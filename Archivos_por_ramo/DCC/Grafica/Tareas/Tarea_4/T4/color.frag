#version 330

//Escriba aquí el color shader
//Debe considerar el material del objeto para obtener el color
//Mire como obtener el material en el Phong shader


out vec4 outColor;

// Material
struct Material {
    vec3 diffuse;
    vec3 ambient;
    vec3 specular;
    float shininess;
};

uniform Material u_material;
uniform vec3 u_viewPos;


void main()
{
    vec3 viewDir = normalize(u_viewPos);

    vec3 result = vec3(0.0);


    //ambient
    vec3 ambient = u_material.ambient * u_material.ambient;

    // diffuse
    
    vec3 diffuse = u_material.diffuse * u_material.diffuse;
    

    // specular 
    
    vec3 halfwayDir = normalize(viewDir);
    float spec = pow(max(dot(viewDir, viewDir), 0.0f), u_material.shininess);
    vec3 specular = u_material.specular * (spec * u_material.specular);

    result += (ambient + diffuse + specular);


	
    outColor = vec4(result, 1.0f);
}

