#version 330

//Escriba aquí el color shader
//Debe considerar el material del objeto para obtener el color
//Mire como obtener el material en el Phong shader

// Si bien no todos son necesarios (se comprobo ejecutando reiteradas veces el programa), se obtienen los valores del vertex shader
in vec3 fragPos;
in vec3 fragNormal;

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

// Uniforms que seran usados, al igual que con los valores de entrada, no todos fueron necesarios
uniform Material u_material;
uniform vec3 u_viewPos;

// Computamos el resultado 
void main()
{
    vec3 normal = normalize(fragNormal);
    vec3 viewDir = normalize(u_viewPos - fragPos);

    // Caracteristica del material material: ambiente (ambient) 
    vec3 ambient = u_material.ambient;

    // Caracteristica del material: difuso (diffuse) 
    vec3 diffuse = u_material.diffuse;
    
    // Caracteristica del material: especular (specular), ademas del brillo (shininess)
    vec3 halfwayDir = normalize(viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular =(spec * u_material.specular);
 
    // Resultado
    vec3 result = vec3(0.0);
    result = (ambient + diffuse + specular);
	
    outColor = vec4(result, 1.0f);
}

/*
Comentarios:
- Se considero solo los parametros del material y se tomo de manera literal las instrucciones del enunciado que hacian referencia a no considerar
  las luces de la escena.

- Se sigue una "estructura" en el calculo a la ecuacion(es) de iluminacion, solo que considerando el material.

- Al computar el resultado final, se trata de la suma de los parametros del material correspondientes al ambiente, difuso, especular y 
  ademas el brillo, esa es la razon del porque al obtener el valor del material "especular" este es diferente al resto, asi se puede
  utilizar el brillo como caracteristica del material.

- Aunque originalmente el template solo tenia el para computar la salida, igual se agregaron valores externos.
*/

