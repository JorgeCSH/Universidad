#version 330
// Notas de autor al final del archivo, ademas de comentarios en el codigo

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


// Directional
struct DirectionalLight {
    vec3 direction;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};


// Pointlight
const int MAX_POINT_LIGHTS = 16;
struct PointLight {
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float constant;
    float linear;
    float quadratic;
};


// Uniforms
uniform Material u_material;
uniform DirectionalLight u_dirLight;
uniform PointLight u_pointLights[MAX_POINT_LIGHTS];
uniform int u_numPointLights;


// Computamos valores para luz direccional 
vec3 computeDirectionalLight(vec3 normal, DirectionalLight light) {
    
    // Ambiental 
    vec3 ambient = light.ambient * u_material.ambient;

    // Difusa
    int N = 4;								// Nuevo: numero de discretizacion.	
    float diff = max(dot(normal, light.direction), 0.0f);
    diff = float(int(diff * float(N))) / float(N);  			// Nuevo: usamos N para discretizar.
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    // Especular (Blinn-Phong segun auxiliares del repositorio), no se toco ademas de para no considerar viewPos 
    vec3 halfwayDir = normalize(light.direction);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular = light.specular * (spec * u_material.specular);

    return (ambient + diffuse + specular);
}


// Computamos valores para luz puntual
vec3 computePointLight(vec3 normal, PointLight light) {
    // Atteunacion
    vec3 lightVec = light.position - fragPos;
    float distance = length(lightVec);
    float attenuation = 1.0f / ( light.linear * distance + light.quadratic * distance * distance + light.constant );

    // Ambiental
    vec3 ambient = light.ambient * u_material.ambient;

    // Difusa
    int N = 4;								// Nuevo: analogo a DirectionalLight.				
    vec3 lightDir = normalize(lightVec);
    float diff = max(dot(normal, lightDir), 0.0f);
    diff = float(int(diff * float(N))) / float(N); 			// Nuevo: analogo a DirectionalLight. 
    vec3 diffuse = light.diffuse * (diff * u_material.diffuse);

    // Especular (Blinn-Phong segun auxiliares del repositorio), no se toco ademas de para no considerar viewPos 
    vec3 halfwayDir = normalize(lightDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0f), u_material.shininess);
    vec3 specular = light.specular * (spec * u_material.specular);

    return (ambient + diffuse + specular) * attenuation;
}

// Calculo final
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

- En el enunciado, si bien no se especificia directamente y solo se hace referencia a la 
  "intensidad de la luz", esta se le daban instrucciones con respecto al componente difuso,
  por ende se decidio discretizar este. Sin embargo es importante destacar que esta se puede
  llevar para otras componentes pues basta con tomar el valor previo al calculo final, es decir,
  el porcentaje de luz declarado como float antes de declarar los resultados como vectores aplicando
  el mismo procedimiento de discretizacion que se llevo en el caso difuso.

- Se tomo como punto de partida el archivo equivalente al PhongShader incluido en el archivo de la
  tarea.

- Se tuvo problemas al desarrollar los cuales se encuentran en el documento principal (main.py). Si
  ademas nota que hay comentarios destacando esto en otros archivos es porque se me olvido borrarlos.
*/

