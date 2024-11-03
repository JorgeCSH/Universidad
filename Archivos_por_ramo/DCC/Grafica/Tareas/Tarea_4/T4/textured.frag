#version 330

//Escriba aquí el textured shader
in vec3 fragPos;
in vec2 fragTexCoord;
in vec3 fragNormal;

out vec4 outColor;

uniform sampler2D u_texture;
uniform vec3 u_lightPosition = vec3(0.0f);
uniform vec3 u_lightColor = vec3(1.0f);

float AMBIENT = 0.15;

float computeLight(vec3 normal, vec3 lightPosition) {
    // attenuation
    vec3 lightVec = lightPosition - fragPos;
    float distance = length(lightVec);
    float attenuation = 1.0f / ( 0.5 * distance * distance );

    // diffuse
    vec3 lightDir = normalize(lightVec);
    float diff = max(dot(normal, lightDir), 0.0f);

    return diff*attenuation;
}

void main() {
    vec4 solidColor = texture(u_texture, fragTexCoord);
    vec3 normal = normalize(fragNormal);
    float amount = computeLight(normal, u_lightPosition);
    vec4 lightColor = vec4(u_lightColor, 1.0f) * max(AMBIENT, amount);
    outColor = lightColor * solidColor;
}
