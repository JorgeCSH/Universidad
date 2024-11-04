#version 330
//Escriba aquí el textured shader

in vec3 fragPos;
in vec2 fragTexCoord;
in vec3 fragNormal;

out vec4 outColor;

uniform vec3 u_lightPosition = vec3(0.0f);
uniform vec3 u_lightColor = vec3(1.0f);
uniform vec3 u_viewPos;

// Material
struct Material {
    vec3 diffuse;
    vec3 ambient;
    vec3 specular;
    float shininess;
};

uniform Material u_material;
uniform sampler2D u_texture;

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
    vec3 halfwayDir = normalize(light.direction+viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular = light.specular * (spec * u_material.specular);

    return (ambient + diffuse + specular);
}



vec3 computePointLight(vec3 normal, vec3 viewDir, PointLight light) {
    // attenuation
    vec3 lightVec = light.position - fragPos;
    float distance = length(lightVec);
    float attenuation_general = 1.0f / ( light.quadratic * distance * distance  );
    float attenuation_set = 1.0f / (0.5 * distance * distance);
	
    // ambient
    vec3 ambient = light.ambient * u_material.ambient;

    // diffuse
    vec3 lightDir = normalize(lightVec);
    float diff = max(dot(normal, lightDir), 0.0f);
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    vec3 halfwayDir = normalize(lightDir+viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular = light.specular * (spec * u_material.specular);

    return (diffuse + ambient + specular) * attenuation_general;
}

void main() {
    vec4 texel = texture(u_texture, fragTexCoord);
    vec3 normal = normalize(fragNormal);
    vec3 result = vec3(0.0);
    vec3 viewDir = normalize(u_viewPos - fragPos);

    result += computeDirectionalLight(normal, viewDir, u_dirLight);
    if (u_numPointLights > 0 && u_numPointLights <= MAX_POINT_LIGHTS) {
        for (int i = 0; i < u_numPointLights; i++)
            result += computePointLight(normal, viewDir, u_pointLights[i]);
    }
    
    outColor = vec4(result, 1.0f) * texel;
}


/*
vec3 computeDirectionalLight(vec3 normal, DirectionalLight light) {
    ???
}

vec3 computePointLight(vec3 normal, PointLight light) {
   ???
}

void main()
{
    outColor = ???
}
*/
