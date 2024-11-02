#version 330

//Escriba aquí el color shader
//Debe considerar el material del objeto para obtener el color
//Mire como obtener el material en el Phong shader

in vec3 fragPos;
in vec3 fragNormal;
//in vec2 fragTexCoord;

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


// Spotlight
const int MAX_SPOT_LIGHTS = 16;
uniform int u_numSpotLights;

struct SpotLight {
    vec3 ambient;
    float outerCutOff;
};

uniform SpotLight u_spotLights[MAX_SPOT_LIGHTS];


// Ambiente pero para direccional
vec3 computeDirectionalLight(vec3 normal, vec3 viewDir, DirectionalLight light) {
    //ambient
    vec3 ambient = light.ambient * u_material.ambient;
    return ambient;
}


// Ambiente pero para Pointlights
vec3 computePointLight(vec3 normal, vec3 viewDir, PointLight light) {
    // attenuation
    vec3 lightVec = light.position - fragPos;
    float distance = length(lightVec);
    float attenuation = 1.0f / ( light.linear * distance + light.quadratic * distance * distance + light.constant );
    
    //ambient
    vec3 ambient = light.ambient * u_material.ambient;
    return ambient*attenuation;
}



// Aca computamos
void main()
{
    vec3 normal = normalize(fragNormal);
    vec3 viewDir = normalize(u_viewPos - fragPos);

    vec3 result = vec3(0.0);

    result += computeDirectionalLight(normal, viewDir, u_dirLight);

    if (u_numPointLights > 0 && u_numPointLights <= MAX_POINT_LIGHTS) {
        for (int i = 0; i < u_numPointLights; i++)
            result += computePointLight(normal, viewDir, u_pointLights[i]);
    }

    outColor = vec4(result, 1.0f);
}

