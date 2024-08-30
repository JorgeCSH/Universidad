import pyglet
import numpy as np
from pyglet.gl import *


WIDTH = 1000
HEIGHT = 1000
DEFINITION = 36
window = pyglet.window.Window(WIDTH, HEIGHT, "Tarea 1 - Sistema Solar")


def crear_planeta(x, y, r, g, b, radius):
    N = DEFINITION
    # Discretizamos un circulo en DEFINITION pasos
    # Cada punto tiene 3 coordenadas y 3 componentes de color
    # Cada triangulo tiene 3 puntos
    # Con N triangulos tenemos 3N puntos
    # El arreglo de posiciones tiene 3 * 3N coordenadas
    # El arreglo de color tiene 3 * 3N componentes
    positions = np.zeros(9*N, dtype=np.float32) 
    colors = np.zeros(9*N, dtype=np.float32)
    dtheta = 2*np.pi / N

    for i in range(N):
        x0 = x + np.cos(i*dtheta)*radius
        y0 = y + np.sin(i*dtheta)*radius
        x1 = x + np.cos((i+1)*dtheta)*radius
        y1 = y + np.sin((i+1)*dtheta)*radius

        # centro
        j = i*9
        positions[j:j+3] = [x, y, 0.0]
        colors[j:j+3] = [r, g, b]
        # p0
        positions[j+3:j+6] = [x0, y0, 0.0]
        colors[j+3:j+6] = [r, g, b]
        # p1
        positions[j+6:j+9] = [x1, y1, 0.0]
        colors[j+6:j+9] = [r, g, b]
        
    return positions, colors


# Funcion que crea la trayectoria de un astro
# x, y: coordenadas del centro del astro
# r, g, b: componentes de color del astro
# radius: radio de la trayectoria
# return: posiciones y colores de la trayectoria
# Discretizamos un circulo en DEFINITION pasos
# No dibuja los radios de los circulos, solo el borde exterior de la trayectoria final
def trayectoria(x, y, r, g, b, radius):
    N = DEFINITION
    positions = np.zeros(9*N, dtype=np.float32)
    colors = np.zeros(9*N, dtype=np.float32)
    dtheta = 2*np.pi / N
    for i in range(N):
        x0 = x + np.cos(i*dtheta)*radius
        y0 = y + np.sin(i*dtheta)*radius
        x1 = x + np.cos((i+1)*dtheta)*radius
        y1 = y + np.sin((i+1)*dtheta)*radius
        j = i*9
        positions[j:j+3] = [x0, y0, 0.0]
        colors[j:j+3] = [r, g, b]
        positions[j+3:j+6] = positions[j:j+3]
        colors[j+3:j+6] = colors[j:j+3]
        positions[j+6:j+9] = [x1, y1, 0.0]
        colors[j+6:j+9] = [r, g, b]
    return positions, colors


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

    vert_program = pyglet.graphics.shader.Shader(vertex_source, "vertex")
    frag_program = pyglet.graphics.shader.Shader(fragment_source, "fragment")
    pipeline = pyglet.graphics.shader.ShaderProgram(vert_program, frag_program)


    # Definimos mediante arreglos los parametros que controlaran a todos los planetas
    # Radio de los planetas
    rr = 1.3*np.array([0.009, 0.015, 0.016, 0.01, 0.05, 0.025, 0.048, 0.02, 0.017])
    # Distancia centro sol a centro planeta
    pos = np.array([0.2, 0.25, 0.31, 0.38, 0.5, 0.7, 0.7, 0.82, 0.9])
    # rel = relativo, corresponde a la suma entre el radio del planeta y la distancia al sol
    rel = pos + rr + np.array([0, 0, 0, 0, 0, 0, float(rr[5])-float(rr[6]), 0, 0])
    # ang corresponde al angulo del planeta con respecto a su orbita (asumiendo circunferencia perfecta)
    ang = np.array([2, 177, 23, 345, 3, 26, 26, 97, 28])
    #cos_arr y sen_arr corresponden al coseno y seno relativo con respecto al angulo de rotacion "ang"
    cos_arr = np.array([np.cos(float(ang[0])), np.cos(float(ang[1])), np.cos(float(ang[2])), np.cos(float(ang[3])), np.cos(float(ang[4])), np.cos(float(ang[5])), np.cos(float(ang[6])), np.cos(float(ang[7])), np.cos(float(ang[8]))])
    sin_arr = np.array([np.sin(float(ang[0])), np.sin(float(ang[1])), np.sin(float(ang[2])), np.sin(float(ang[3])), np.sin(float(ang[4])), np.sin(float(ang[5])), np.sin(float(ang[6])), np.sin(float(ang[7])), np.sin(float(ang[8]))])
    #relc y rels corresponden a la proyeccion en coseno (relc) y seno (rels) del relativo con respecto a los angulos
    relc = rel*cos_arr
    rels = rel*sin_arr

    # Arreglos para las lunas de marte, contienen el radio de las lunas y la proyeccion del radio del planeta mas una constante
    pho = np.array([0.003, (float(rr[3])+0.005)*np.cos(10), (float(rr[3])+0.005)*np.sin(10)])
    dei = np.array([0.002, (float(rr[3])+0.01)*np.cos(70), (float(rr[3])+0.01)*np.sin(70)])


    # Usamos la funcion crear_planeta para crear los planetas (o cualquier otro astro) del sistema solar
    # Corresponde al sol
    position_sol, color_sol = crear_planeta(0, 0, 1, 1, 0, 0.15)


    # Usamos la funcion trayectoria para crear las trayectorias de los planetas (solo la tierra segun solicitado)
    position_trayectoria_tierra, color_trayectoria_tierra = trayectoria(0, 0, 1, 1, 1, float(rel[2]))


    # Usamos la funcion crear_planeta para crear los planetas
    # Mercurio
    position_mercurio, color_mercurio = crear_planeta(float(relc[0]), float(rels[0]), 66/255, 43/255, 1/255, float(rr[0]))
    # Venus
    position_venus, color_venus = crear_planeta(float(relc[1]), float(rels[1]), 215/255, 141/255, 1/255, float(rr[1]))
    # Tierra
    position_tierra, color_tierra = crear_planeta(float(relc[2]), float(rels[2]), 0, 1, 0, float(rr[2]))
    # Marte
    position_marte, color_marte = crear_planeta(float(relc[3]), float(rels[3]), 1, 0, 0, float(rr[3]))
    # Jupiter
    position_jupiter, color_jupiter = crear_planeta(float(relc[4]), float(rels[4]), 255/255, 147/255, 0/255, float(rr[4]))
    # Saturno, los anillos se hacen superponiendo dos circulos de radio distinto
    position_saturno, color_saturno = crear_planeta(float(relc[5]), float(rels[5]), 233/255, 108/255, 0/255, float(rr[5]))
    position_anillos, color_anillos = crear_planeta(float(relc[6]), float(rels[6]), 96/255, 96/255, 96/255, float(rr[6]))
    # Urano
    position_unranus, color_unranus = crear_planeta(float(relc[7]), float(rels[7]), 123/255, 163/255, 254/255, float(rr[7]))
    # Neptuno
    position_nepturno, color_neptuno = crear_planeta(float(relc[8]), float(rels[8]), 0, 0, 1, float(rr[8]))

    # Corresponde a las lunas de marte
    position_phobos, color_phobos = crear_planeta(float(relc[3])+float(pho[1]), float(rels[3])+float(pho[2]), 175/255, 145/255, 144/255, float(pho[0]))
    position_deimos, color_deimos = crear_planeta(float(relc[3])+float(dei[1]), float(rels[3])+float(dei[2]), 206/255, 173/255, 141/255, float(dei[0]))


    sol = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)

    trayectoria_tierra = pipeline.vertex_list(3*DEFINITION, GL_LINE_LOOP)

    mercurio = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    venus = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    tierra = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    marte = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    jupiter = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    saturno = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    anillos = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    urano = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    neptuno = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)

    phobos = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    deimos = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)


    sol.position[:] = position_sol
    sol.color[:] = color_sol
    trayectoria_tierra.position[:] = position_trayectoria_tierra
    trayectoria_tierra.color[:] = color_trayectoria_tierra

    mercurio.color[:] = color_mercurio
    venus.color[:] = color_venus
    tierra.color[:] = color_tierra
    marte.color[:] = color_marte
    jupiter.color[:] = color_jupiter
    saturno.color[:] = color_saturno
    anillos.color[:] = color_anillos
    urano.color[:] = color_unranus
    neptuno.color[:] = color_neptuno

    phobos.color[:] = color_phobos
    deimos.color[:] = color_deimos


    @window.event
    def on_draw():
        glClearColor(0.1, 0.1, 0.1, 0.0)
        with pipeline:

            trayectoria_tierra.draw(GL_LINE_LOOP)
            sol.draw(GL_TRIANGLES)

            mercurio.draw(GL_TRIANGLES)
            venus.draw(GL_TRIANGLES)
            tierra.draw(GL_TRIANGLES)
            marte.draw(GL_TRIANGLES)
            phobos.draw(GL_TRIANGLES)
            deimos.draw(GL_TRIANGLES)
            jupiter.draw(GL_TRIANGLES)

            anillos.draw(GL_TRIANGLES)
            saturno.draw(GL_TRIANGLES)

            urano.draw(GL_TRIANGLES)
            neptuno.draw(GL_TRIANGLES)



    @window.event
    def update(dt):
        global time
        trayectoria_tierra.position[:] = position_trayectoria_tierra
        mercurio.position[:] = position_mercurio
        venus.position[:] = position_venus
        tierra.position[:] = position_tierra
        marte.position[:] = position_marte
        phobos.position[:] = position_phobos
        deimos.position[:] = position_deimos
        jupiter.position[:] = position_jupiter
        saturno.position[:] = position_saturno
        anillos.position[:] = position_anillos
        neptuno.position[:] = position_nepturno
        urano.position[:] = position_unranus
        #time = time**dt

    update(dt = 1/60)
    pyglet.app.run()

    
