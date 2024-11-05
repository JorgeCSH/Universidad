#version 330
in vec3 fragPos;
flat in vec3 fragNormal;
in vec2 fragTexCoord;

out vec4 outColor;

// Material
struct Material {
    vec3 diffuse;
    vec3 ambient;
    vec3 specular;
    float shininess;
};

uniform Material u_material;


// Directional
struct DirectionalLight {
    vec3 direction;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

uniform DirectionalLight u_dirLight;

// Pointlight
const int MAX_POINT_LIGHTS = 16;
uniform int u_numPointLights;

struct PointLight {
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float constant;
    float linear;
    float quadratic;
};

uniform PointLight u_pointLights[MAX_POINT_LIGHTS];

//funcion que procesa directional light
vec3 computeDirectionalLight(vec3 normal, DirectionalLight light) {
    //ambient
    vec3 ambient = light.ambient * u_material.ambient;

    // diffuse
    float diff = max(dot(normal, light.direction), 0.0f);
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    return (ambient + diffuse);
}


//funcion que procesa pointlight
vec3 computePointLight(vec3 normal, PointLight light) {
    // attenuation
    vec3 lightVec = light.position - fragPos;
    float distance = length(lightVec);
    float attenuation = 1.0f / ( light.linear * distance + light.quadratic * distance * distance + light.constant );

    // ambient
    vec3 ambient = light.ambient * u_material.ambient;

    // diffuse
    vec3 lightDir = normalize(lightVec);
    float diff = max(dot(normal, lightDir), 0.0f);
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    //return (ambiebt + diffuse) * attenuation; 
    return (ambient + diffuse);
}


void main()
{
    vec3 normal = normalize(fragNormal);
    vec3 result = vec3(0.0);

    result += computeDirectionalLight(normal, u_dirLight);

    if (u_numPointLights > 0 && u_numPointLights <= MAX_POINT_LIGHTS) {
        for (int i = 0; i < u_numPointLights; i++)
            result += computePointLight(normal, u_pointLights[i]);
    }

    outColor = vec4(result, 1.0f);
}

/* 
Notas de autor:
- Un error que se tuvo al realizar este shader fue que, al cargarlo este no cargaba las sombras de la parte que 
  no daban al sol. Si bien se considero un posible error ocurrio que cuando se cambio el shader para que todos
  utilizaran el mismo, este ultimo cargaba bien, mas aun, si se cambiaba el phong shader por el flat shader, 
  este cargaba bien (cambiar el nombre flat_pipeline por phong_pipeline y vicerversa para que al cargar uno se 
  carge el otro).

- El mismo error de la variable "attenuation" se tuvo en este shader.
*/
