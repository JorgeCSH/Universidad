'''
Información del trabajo:
Autor: Jorge Cummins
RUT: 21353175-1
Curso: CC3501-1
Profesor: Ivan Sipiran
Fecha: 28 de agosto de 2024

Con respecto a la tarea: esta fue realizada en el mismo código originalmente otorgado por el cuerpo docente, el cual
fue editado. Los cuadros separados por # corresponden a títulos y secciones, además de comentarios. El código
probablemente, tenga una cantidad notoria de comentarios que de llegar a ser molestos puedo reducirlos para la siguiente
entrega (en introducción a la programación solía enviar un .txt por separado para evitar justamente que sea engorroso).
Cualquier comentario es totalmente bienvenido.

Otra cosa que me gustaria agregar es solicitar si hay algun problema con que para los cuadros de comentario mezcle los
"""""" y # o no, para evitar complicaciones futuras.
'''

# Seccion 1: configuracion ############################################################################################
#######################################################################################################################
# Importamos las librerias que seran utilizadas (son las mismas que venian en el codigo original)
import pyglet
import numpy as np
from pyglet.gl import *

# Definimos los parametros de la ventana
WIDTH = 1000
HEIGHT = 1000
DEFINITION = 72

window = pyglet.window.Window(WIDTH, HEIGHT, "Tarea 1 - Sistema Solar")

# Seccion 2: funciones ################################################################################################
#######################################################################################################################
'''
Función crear_planeta
Función entregada por el cuerpo docente, específicamente esta no fue modificada.
'''


def crear_planeta(x, y, r, g, b, radius):
    N = DEFINITION
    # Discretizamos un circulo en DEFINITION pasos
    # Cada punto tiene 3 coordenadas y 3 componentes de color
    # Cada triangulo tiene 3 puntos
    # Con N triangulos tenemos 3N puntos
    # El arreglo de posiciones tiene 3 * 3N coordenadas
    # El arreglo de color tiene 3 * 3N componentes
    positions = np.zeros(9 * N, dtype=np.float32)
    colors = np.zeros(9 * N, dtype=np.float32)
    dtheta = 2 * np.pi / N

    for i in range(N):
        x0 = x + np.cos(i * dtheta) * radius
        y0 = y + np.sin(i * dtheta) * radius
        x1 = x + np.cos((i + 1) * dtheta) * radius
        y1 = y + np.sin((i + 1) * dtheta) * radius

        # centro
        j = i * 9
        positions[j:j + 3] = [x, y, 0.0]
        colors[j:j + 3] = [r, g, b]
        # p0
        positions[j + 3:j + 6] = [x0, y0, 0.0]
        colors[j + 3:j + 6] = [r, g, b]
        # p1
        positions[j + 6:j + 9] = [x1, y1, 0.0]
        colors[j + 6:j + 9] = [r, g, b]

    return positions, colors


"""
Función trayectoria
Esta función corresponde a una modificación de la función "crear_planeta" entregada por el cuerpo docente.
La función en cuestión realiza la misma "función" que la función "crear_planeta", pero a la hora de devolver el arreglo
de coordenadas de triángulos, devuelve un arreglo donde la coordenada x del centro se iguala con los del x0, de esta
forma se busca no dibujar el rastro que serían equivalentes a los "radios" del círculo y solamente la 
base/borde externo.

La función recibe las coordenadas x, y del centro de la circunferencia (se aproxima la trayectoria de un planeta a una 
circunferencia), los valores rgb de los colores y el radio de la circunferencia, retornando una tupla con un arreglo de
coordenadas y un arreglo de colores.
"""
def trayectoria(x, y, r, g, b, radius):
    N = DEFINITION
    positions = np.zeros(9 * N, dtype=np.float32)
    colors = np.zeros(9 * N, dtype=np.float32)
    dtheta = 2 * np.pi / N
    for i in range(N):
        x0 = x + np.cos(i * dtheta) * radius
        y0 = y + np.sin(i * dtheta) * radius
        x1 = x + np.cos((i + 1) * dtheta) * radius
        y1 = y + np.sin((i + 1) * dtheta) * radius
        j = i * 9
        positions[j:j + 3] = [x0, y0, 0.0]  # Posicion donde estarian las coordenadas del centro se igualan a x0
        colors[j:j + 3] = [r, g, b]  # Se iguala el color tambien
        positions[j + 3:j + 6] = positions[
                                 j:j + 3]  # Como se igualaron los valores, se toma el mismo arreglo para el punto x0
        colors[j + 3:j + 6] = colors[
                              j:j + 3]  # Como se igualaron los valores, se toma el mismo arreglo para los colores
        positions[j + 6:j + 9] = [x1, y1,
                                  0.0]  # Punto extra, se mantiene igual a x1 y permite realizar la trayectoria x0-x1
        colors[j + 6:j + 9] = [r, g, b]  # Colores del punto x1
    return positions, colors


# Seccion 3: implementacion ###########################################################################################
#######################################################################################################################
# Creamos los shaders, esta parte no fue modificada hasta la parte donde se compilan los shaders.
if __name__ == "__main__":
    vertex_source = """
#version 330

in vec3 position;
in vec3 color;

out vec3 fragColor;

void main() {
    fragColor = color;
    gl_Position = vec4(position, 1.0f);
}
    """

    fragment_source = """
#version 330

in vec3 fragColor;
out vec4 outColor;

void main()
{
    outColor = vec4(fragColor, 1.0f);
}
    """
    # Previo a crear el sistema solar, configuramos.
    # Compilamos los shaders
    vert_program = pyglet.graphics.shader.Shader(vertex_source, "vertex")
    frag_program = pyglet.graphics.shader.Shader(fragment_source, "fragment")
    pipeline = pyglet.graphics.shader.ShaderProgram(vert_program, frag_program)

    '''
    Esta parte es media confusa, por ende explicaré un poco más detallado antes de entrar a los comentarios aparte.
    Para dibujar el sistema solar, en vez de añadir un dato para cada planeta/astro/trayectoria, se optó por dejar 
    la función y su llamado a parte y los valores (menos los colores) en arreglos. La idea era poder modificar las 
    caracteristicas de un planeta alterando solo el valor del arreglo, esto permitió añadir interacciones para el 
    desarrollo que eran más cómodas de realizar. Un ejemplo de esto fue que al mover el sol se mueven todos los demás
    componentes del sistema y sin editar nada, puesto a que en los arreglos esta todo previamente editado.

    En caso de ser incómodo o directamente que no sea de agrado, no tengo problema en no realizar esto para la próxima 
    tarea.

    Ahora, para evitar incluir esta información en cada oportunidad, en el código los anillos de saturno se dibujan
    superponiendo dos círculos, uno más grande que simula los anillos y otro más pequeño que simula a saturno. Los datos
    de estos círculos se encuentran seguidos en el arreglo rel, donde rel[5] corresponde al planeta saturno y rel[6] a
    los anillos. Al dibujarlos se ubican en una misma posición dibujando los anillos antes que el planeta.
    '''
    # Arreglo del sol (data_sol): posee la coordenada x, coordenada y, radio respectivamente.
    data_sol = np.array([0, 0, 0.15])
    # Radio de los planetas (rr): posee los radios de los planetas oordenados de mercurio a neptuno respectivamente.
    rr = 1.3 * np.array([0.009, 0.015, 0.016, 0.01, 0.05, 0.025, 0.048, 0.02, 0.017])
    # Distancia entre el sol y el planeta (pos): posee la distancia entre el sol y los planetas ordenados de mercurio a
    # neptuno.
    pos = np.array([0.2, 0.25, 0.31, 0.38, 0.5, 0.7, 0.7, 0.82, 0.9])
    # Posicion relativa (rel): posicion relativa de los planetas y su radio con respecto al sol.
    rel = pos + rr + np.array([0, 0, 0, 0, 0, 0, float(rr[5]) - float(rr[6]), 0, 0])
    # Angulo (ang): posee el angulo entre la orbita (trayectoria) de los planetas con respecto al sol.
    ang = np.array([1.2 * np.pi, 0.12, 0.9 * np.pi, 0.6 * np.pi, -0.12, 0.7 * np.pi, 0.7 * np.pi, 1.13 * np.pi, np.pi])
    # Arreglos trigonometricos (cos_arr, sin_arr): poseen los valores de coseno y seno de los angulos para cada planeta.
    cos_arr = np.array([np.cos(float(ang[0])), np.cos(float(ang[1])), np.cos(float(ang[2])), np.cos(float(ang[3])),
                        np.cos(float(ang[4])), np.cos(float(ang[5])), np.cos(float(ang[6])), np.cos(float(ang[7])),
                        np.cos(float(ang[8]))])
    sin_arr = np.array([np.sin(float(ang[0])), np.sin(float(ang[1])), np.sin(float(ang[2])), np.sin(float(ang[3])),
                        np.sin(float(ang[4])), np.sin(float(ang[5])), np.sin(float(ang[6])), np.sin(float(ang[7])),
                        np.sin(float(ang[8]))])
    # proyecciones (relc, rels): poseen las proyecciones de las posiciones relativas de los planetas con respecto al
    # sol, se le suma ademas la posicion x e y del sol.
    relc = rel * cos_arr + float(data_sol[0]) * np.ones(9)  # Proyeccion eje x
    rels = rel * sin_arr + float(data_sol[1]) * np.ones(9)  # Proyeccion eje y

    # *EXTRAS* Arreglos para las lunas de marte
    # Arreglo de phobos: posee el radio, la proyeccion x y la proyeccion y de phobos CON RESPECTO A MARTE (se mueven junto a el).
    pho = np.array([0.003, (float(rr[3]) + 0.007) * np.cos(10), (float(rr[3]) + 0.007) * np.sin(10)])
    # Arreglo de deimos: posee el radio, la proyeccion x y la proyeccion y de deimos, tambien RESPECTO A MARTE.
    dei = np.array([0.002, (float(rr[3]) + 0.01) * np.cos(70), (float(rr[3]) + 0.01) * np.sin(70)])

    '''
    En esta parte llamamos a la función crear_planeta y trayectoria para crear la imagen. Usamos los valores de los 
    arreglos, llamándolos generalmente con la forma float(arreglo[i]) para cada valor. La única excepción es saturno,
    el cual se dibuja con dos círculos superpuestos para simular los anillos, donde se realiza un planeta más grande
    para los anillos con el mismo centro de otro más pequeño que simula a saturno.
    '''
    # Creamos el sol usando la funcion crear_planeta
    position_sol, color_sol = crear_planeta(float(data_sol[0]), float(data_sol[1]), 1, 1, 0, float(data_sol[2]))

    # Usamos la funcion trayectoria para crear las trayectorias de los planetas.
    # Mercurio.
    position_trayectoria_mercurio, color_trayectoria_mercurio = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[0]))
    # Venus.
    position_trayectoria_venus, color_trayectoria_venus = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[1]))
    # Tierra.
    position_trayectoria_tierra, color_trayectoria_tierra = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,float(rel[2]))
    # Marte.
    position_trayectoria_marte, color_trayectoria_marte = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[3]))
    # Jupiter.
    position_trayectoria_jupiter, color_trayectoria_jupiter = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[4]))
    # Saturno.
    position_trayectoria_saturno, color_trayectoria_saturno = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[5]))
    # Urano.
    position_trayectoria_urano, color_trayectoria_urano = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[7]))
    # Neptuno.
    position_trayectoria_neptuno, color_trayectoria_neptuno = trayectoria(float(data_sol[0]), float(data_sol[1]), 1, 1, 1,
                                                                        float(rel[8]))

    # Usamos la funcion crear_planeta para crear el resto de los planetas.
    # Mercurio.
    position_mercurio, color_mercurio = crear_planeta(float(relc[0]), float(rels[0]), 66 / 255, 43 / 255, 1 / 255,
                                                      float(rr[0]))
    # Venus.
    position_venus, color_venus = crear_planeta(float(relc[1]), float(rels[1]), 215 / 255, 141 / 255, 1 / 255,
                                                float(rr[1]))
    # Tierra.
    position_tierra, color_tierra = crear_planeta(float(relc[2]), float(rels[2]), 0, 1, 0, float(rr[2]))
    # Marte.
    position_marte, color_marte = crear_planeta(float(relc[3]), float(rels[3]), 1, 0, 0, float(rr[3]))
    # Jupiter.
    position_jupiter, color_jupiter = crear_planeta(float(relc[4]), float(rels[4]), 255 / 255, 147 / 255, 0 / 255,
                                                    float(rr[4]))
    # Saturno, los anillos se hacen superponiendo dos circulos de radio distinto.
    position_saturno, color_saturno = crear_planeta(float(relc[5]), float(rels[5]), 233 / 255, 108 / 255, 0 / 255,
                                                    float(rr[5]))
    position_anillos, color_anillos = crear_planeta(float(relc[6]), float(rels[6]), 96 / 255, 96 / 255, 96 / 255,
                                                    float(rr[6]))
    # Urano.
    position_urano, color_urano = crear_planeta(float(relc[7]), float(rels[7]), 123 / 255, 163 / 255, 254 / 255,
                                                float(rr[7]))
    # Neptuno.
    position_nepturno, color_neptuno = crear_planeta(float(relc[8]), float(rels[8]), 0, 0, 1, float(rr[8]))

    # *EXTRA* Creamos las lunas de marte.
    # Phobos.
    position_phobos, color_phobos = crear_planeta(float(relc[3]) + float(pho[1]), float(rels[3]) + float(pho[2]),
                                                  175 / 255, 145 / 255, 144 / 255, float(pho[0]))
    # Deimos.
    position_deimos, color_deimos = crear_planeta(float(relc[3]) + float(dei[1]), float(rels[3]) + float(dei[2]),
                                                  206 / 255, 173 / 255, 141 / 255, float(dei[0]))

    '''
    En esta parte cargamos los datos de los planetas para poder ser dibujados en la ventana.
    '''
    # Creamos en la GPU (segun la terminologia usada en clase auxiliar).
    # Creamos el sol.
    sol = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)

    # Creamos la trayectoria de los planetas.
    # Mercurio.
    trayectoria_mercurio = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Venus.
    trayectoria_venus = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Tierra.
    trayectoria_tierra = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Marte.
    trayectoria_marte = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Jupiter.
    trayectoria_jupiter = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Saturno.
    trayectoria_saturno = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Urano.
    trayectoria_urano = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)
    # Neptuno.
    trayectoria_neptuno = pipeline.vertex_list(3 * DEFINITION, GL_LINE_LOOP)

    # Creamos los planetas.
    # Mercurio.
    mercurio = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Venus.
    venus = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Tierra.
    tierra = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Marte.
    marte = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Jupiter.
    jupiter = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Saturno.
    saturno = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    anillos = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Urano.
    urano = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Neptuno.
    neptuno = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)

    # *EXTRA* Creamos las lunas de marte.
    # Phobos.
    phobos = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)
    # Deimos.
    deimos = pipeline.vertex_list(3 * DEFINITION, GL_TRIANGLES)

    '''
    En esta parte, copiamos los datos de la posicion y colores que seran dibujados en la ventana.
    '''
    # Datos sol.
    # Posicion.
    sol.position[:] = position_sol
    # Color.
    sol.color[:] = color_sol

    # Datos trayectorias.
    # Mercurio.
    trayectoria_mercurio.position[:] = position_trayectoria_mercurio
    trayectoria_mercurio.color[:] = color_trayectoria_mercurio
    # Venus.
    trayectoria_venus.position[:] = position_trayectoria_venus
    trayectoria_venus.color[:] = color_trayectoria_venus
    # Tierra.
    trayectoria_tierra.position[:] = position_trayectoria_tierra
    trayectoria_tierra.color[:] = color_trayectoria_tierra
    # Marte.
    trayectoria_marte.position[:] = position_trayectoria_marte
    trayectoria_marte.color[:] = color_trayectoria_marte
    # Jupiter.
    trayectoria_jupiter.position[:] = position_trayectoria_jupiter
    trayectoria_jupiter.color[:] = color_trayectoria_jupiter
    # Saturno.
    trayectoria_saturno.position[:] = position_trayectoria_saturno
    trayectoria_saturno.color[:] = color_trayectoria_saturno
    # Urano.
    trayectoria_urano.position[:] = position_trayectoria_urano
    trayectoria_urano.color[:] = color_trayectoria_urano
    # Neptuno.
    trayectoria_neptuno.position[:] = position_trayectoria_neptuno
    trayectoria_neptuno.color[:] = color_trayectoria_neptuno

    # Datos planetas.
    # Mercurio.
    mercurio.position[:] = position_mercurio
    mercurio.color[:] = color_mercurio
    # Venus.
    venus.position[:] = position_venus
    venus.color[:] = color_venus
    # Tierra.
    tierra.position[:] = position_tierra
    tierra.color[:] = color_tierra
    # Marte.
    marte.position[:] = position_marte
    marte.color[:] = color_marte
    # Jupiter.
    jupiter.position[:] = position_jupiter
    jupiter.color[:] = color_jupiter
    # Saturno.
    saturno.position[:] = position_saturno
    anillos.position[:] = position_anillos
    saturno.color[:] = color_saturno
    anillos.color[:] = color_anillos
    # Urano.
    urano.position[:] = position_urano
    urano.color[:] = color_urano
    # Neptuno.
    neptuno.position[:] = position_nepturno
    neptuno.color[:] = color_neptuno

    # *EXTRA* Colores de las lunas de marte.
    # Phobos.
    phobos.position[:] = position_phobos
    phobos.color[:] = color_phobos
    # Deimos.
    deimos.position[:] = position_deimos
    deimos.color[:] = color_deimos

    '''
    En esta parte, agregamos los datos de la posición de los elementos que serán dibujados en la ventana.
    '''


    @window.event
    def on_draw():
        glClearColor(0.1, 0.1, 0.1, 0.0)
        with pipeline:
            # Dibujamos el sol.
            sol.draw(GL_TRIANGLES)

            # Dibujamos las trayectorias.
            # Mercurio.
            trayectoria_mercurio.draw(GL_LINE_LOOP)
            # Venus.
            trayectoria_venus.draw(GL_LINE_LOOP)
            # Tierra.
            trayectoria_tierra.draw(GL_LINE_LOOP)
            # Marte.
            trayectoria_marte.draw(GL_LINE_LOOP)
            # Jupiter.
            trayectoria_jupiter.draw(GL_LINE_LOOP)
            # Saturno.
            trayectoria_saturno.draw(GL_LINE_LOOP)
            # Urano.
            trayectoria_urano.draw(GL_LINE_LOOP)
            # Neptuno.
            trayectoria_neptuno.draw(GL_LINE_LOOP)

            # Dibujamos los planetas.
            # Mercurio.
            mercurio.draw(GL_TRIANGLES)
            # Venus.
            venus.draw(GL_TRIANGLES)
            # Tierra.
            tierra.draw(GL_TRIANGLES)
            # Marte.
            marte.draw(GL_TRIANGLES)
            # Jupiter.
            jupiter.draw(GL_TRIANGLES)
            # Saturno.
            anillos.draw(GL_TRIANGLES)
            saturno.draw(GL_TRIANGLES)
            # Urano.
            urano.draw(GL_TRIANGLES)
            # Neptuno.
            neptuno.draw(GL_TRIANGLES)

            # *EXTRA* Dibujamos las lunas de marte.
            # Phobos.
            phobos.draw(GL_TRIANGLES)
            # Deimos.
            deimos.draw(GL_TRIANGLES)


    # Esta funcion (update()) originalment iba a tener los planetas.position, sin embargo y pese a que el resultado
    # hubiera sido el mismo, se decidio dejar vacia para seguir el mismo formato que el ejemplo del codigo original.
    @window.event
    def update(dt):
        pass


    pyglet.app.run()

# Seccion 4: final ####################################################################################################
'''
Para finalizar, agrego el cómo ejecute la tarea durante su desarrollo:
-> Windows 10: editado en pycharm y ejecutado tanto en la terminal activando el environment "conda activate python-cg".
-> Windows 10: editado en pycharm y ejecutando el codigo con la opcion default de pycharm.
-> Linux (debian12): editado en neovim (nvim) y ejecutado desde la terminal con el environment "source ~/python-cg/bin/activate".

Cualquier comentario se agradecerían para poder mejorar futuros desarrollos.
'''