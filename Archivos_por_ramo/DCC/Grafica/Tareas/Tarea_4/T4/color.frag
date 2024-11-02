#version 330

//Escriba aquí el color shader
//Debe considerar el material del objeto para obtener el color
//Mire como obtener el material en el Phong shader
/* 
Este fragemt shader tiene que recibir un material y devolver el color, no considera
la iluminacion, solo el color
*/


//Inputs del vertex shader (basic.vert)
in vec3 fragNormal;
in vec3 fragPos;
in vec2 fragTexCoord;

//Output del fragment shader
out vec4 outColor;

//Material del objeto
struct Material {
    vec3 diffuse;
    vec3 ambient;
    vec3 specular;
    float shininess;
};

uniform Material u_material;
sssssss

void main() {
    
		    
    vec3 result = u_material.ambient;
    outColor = vec4(result, 1.0f);
} 
