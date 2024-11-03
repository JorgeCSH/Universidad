#version 330

//Escriba aquí el color shader
//Debe considerar el material del objeto para obtener el color
//Mire como obtener el material en el Phong shader
/*
void main() {
    
    outColor =  ???
}
*/


in vec3 fragNormal;
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

// Lighting
uniform vec3 u_viewPos;

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

vec3 computeDirectionalLight(vec3 normal, vec3 viewDir, DirectionalLight light) {
    //ambient
    vec3 ambient = light.ambient * u_material.ambient;

    // diffuse
    
    float diff = max(dot(normal, light.direction), 0.0f);
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);
    

    // specular blinn phong
    
    vec3 halfwayDir = normalize(light.direction + viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular = light.specular * (spec * u_material.specular);
    

    //specular phong

    
    vec3 R = -light.direction - 2*dot(-light.direction, normal) * normal;
    float specPhong = max(dot(R, viewDir), 0.0f);
    specPhong = pow(specPhong, u_material.shininess);
    vec3 specularPhong = light.specular * (specPhong * u_material.specular);
    

    return (ambient + diffuse + specular);
}

vec3 computePointLight(PointLight light) {

    // ambient
    vec3 ambient = light.ambient * u_material.ambient;

    return ambient;
}


void main()
{
    vec3 normal = normalize(fragNormal);
    vec3 viewDir = normalize(u_viewPos);

    vec3 result = vec3(0.0);

    result += computeDirectionalLight(normal, viewDir, u_dirLight);

    if (u_numPointLights > 0 && u_numPointLights <= MAX_POINT_LIGHTS) {
        for (int i = 0; i < u_numPointLights; i++)
            result += computePointLight(u_pointLights[i]);
    }

    outColor = vec4(result, 1.0f);
}

