#version 330
// Se define el valor/vector con los parametros de salida
out vec4 outColor;

// Siguiendo las instrucciones, se siguio lo realizado en el phong shader para obtener los materiales
// Material
struct Material {
    vec3 diffuse;
    vec3 ambient;
    vec3 specular;
    float shininess;
};


// Definimos uniform del material
uniform Material u_material;


// Computamos el resultado 
void main()
{
 
    // Resultado
    vec3 result = vec3(0.0);
    //result = (ambient + diffuse + specular);
    result = (u_material.ambient + u_material.diffuse + u_material.specular);	
    outColor = vec4(result, 1.0f);
}

/*
Comentarios:
- Se considero solo los parametros del material y se tomo de manera literal las instrucciones del enunciado que hacian referencia a no considerar
  las luces de la escena.
*/

