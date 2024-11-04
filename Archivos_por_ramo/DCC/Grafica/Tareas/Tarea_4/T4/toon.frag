#version 330
//Escriba aquí su toon shader
//Para más indicaciones lea el enunciado
/*
Tome el Phong shader como un punto de partida
*/


in vec3 fragPos;
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

float discretize(float value, int N) {
    // Clamp value to [0, 1]
    value = clamp(value, 0.0, 1.0);
    // Scale to [0, N-1], round to nearest integer, then scale back to [0, 1]
    return floor(value * float(N)) / float(N - 1);
}

vec3 computeDirectionalLight(vec3 normal, vec3 viewDir, DirectionalLight light, int N) {
    // Ambient light
    vec3 ambient = light.ambient * u_material.ambient;

    // Diffuse light
    float diff = max(dot(normal, light.direction), 0.0f);
    diff = discretize(diff, N); // Discretize the diffuse intensity
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    // Specular Blinn-Phong
    vec3 halfwayDir = normalize(light.direction + viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    spec = discretize(spec, N); // Discretize the specular intensity
    vec3 specular = light.specular * (spec * u_material.specular);

    // Combine components
    return ambient + diffuse + specular;
}
vec3 computePointLight(vec3 normal, vec3 viewDir, PointLight light, int N) {
    // Attenuation
    vec3 lightVec = light.position - fragPos;
    float distance = length(lightVec);
    float attenuation = 1.0f / (light.linear * distance + light.quadratic * distance * distance + light.constant);

    // Ambient light
    vec3 ambient = light.ambient * u_material.ambient;

    // Diffuse light
    vec3 lightDir = normalize(lightVec);
    float diff = max(dot(normal, lightDir), 0.0f);
    diff = discretize(diff, N); // Discretize the diffuse intensity
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    // Specular Blinn-Phong
    vec3 halfwayDir = normalize(lightDir + viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    spec = discretize(spec, N); // Discretize the specular intensity
    vec3 specular = light.specular * (spec * u_material.specular);

    // Combine components and apply attenuation
    return (ambient + diffuse + specular);
}




/*
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

vec3 computePointLight(vec3 normal, vec3 viewDir, PointLight light) {
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

    // specular blinn phong
    vec3 halfwayDir = normalize(lightDir + viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular = light.specular * (spec * u_material.specular);

    return (ambient + diffuse + specular) * attenuation;
}

*/
void main()
{
    vec3 normal = normalize(fragNormal);
    vec3 viewDir = normalize(u_viewPos - fragPos);
    int N = 7;
    vec3 result = vec3(0.0);

    result += computeDirectionalLight(normal, viewDir, u_dirLight, N);

    if (u_numPointLights > 0 && u_numPointLights <= MAX_POINT_LIGHTS) {
        for (int i = 0; i < u_numPointLights; i++)
            result += computePointLight(normal, viewDir, u_pointLights[i], N);
    }

    outColor = vec4(result, 1.0f);
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

