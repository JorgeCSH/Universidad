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


    rr = np.array([0.007, 0.015, 0.016, 0.01, 0.05, 0.025, 0.048, 0.02, 0.017])
    pos = np.array([0.2, 0.25, 0.3, 0.35, 0.5, 0.7, 0.7, 0.82, 0.9])
    rel = pos + rr + np.array([0, 0, 0, 0, 0, 0, float(rr[5])-float(rr[6]), 0, 0])
    ang = np.array([2, 177, 23, 2865, 3, 26, 26, 97, 28])
    cos_arr = np.array([np.cos(float(ang[0])), np.cos(float(ang[1])), np.cos(float(ang[2])), np.cos(float(ang[3])), np.cos(float(ang[4])), np.cos(float(ang[5])), np.cos(float(ang[6])), np.cos(float(ang[7])), np.cos(float(ang[8]))])
    sin_arr = np.array([np.sin(float(ang[0])), np.sin(float(ang[1])), np.sin(float(ang[2])), np.sin(float(ang[3])), np.sin(float(ang[4])), np.sin(float(ang[5])), np.sin(float(ang[6])), np.sin(float(ang[7])), np.sin(float(ang[8]))])
    relc = rel*cos_arr
    rels = rel*sin_arr


    position_yang, color_yang = crear_planeta(0, 0, 1, 1, 1, 0.32)
    position_yin, color_yin = crear_planeta(0, 0, 0, 0, 0, 0.319)
    position_sol, color_sol = crear_planeta(0, 0, 1, 1, 0, 0.15)

    position_mercurio, color_mercurio = crear_planeta(float(relc[0]), float(rels[0]), 66/255, 43/255, 1/255, float(rr[0]))
    position_venus, color_venus = crear_planeta(float(relc[1]), float(rels[1]), 215/255, 141/255, 1/255, float(rr[1]))
    position_tierra, color_tierra = crear_planeta(float(relc[2]), float(rels[2]), 0, 1, 0, float(rr[2]))
    position_marte, color_marte = crear_planeta(float(relc[3]), float(rels[3]), 1, 0, 0, float(rr[3]))
    position_jupiter, color_jupiter = crear_planeta(float(relc[4]), float(rels[4]), 255/255, 147/255, 0/255, float(rr[4]))
    position_saturno, color_saturno = crear_planeta(float(relc[5]), float(rels[5]), 233/255, 108/255, 0/255, float(rr[5]))
    position_anillos, color_anillos = crear_planeta(float(relc[6]), float(rels[6]), 96/255, 96/255, 96/255, float(rr[6]))
    position_unranus, color_unranus = crear_planeta(float(relc[7]), float(rels[7]), 123/255, 163/255, 254/255, float(rr[7]))
    position_nepturno, color_neptuno = crear_planeta(float(relc[8]), float(rels[8]), 0, 0, 1, float(rr[8]))



    yang = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    yin = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    sol = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)

    mercurio = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    venus = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    tierra = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    marte = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    jupiter = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    saturno = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    anillos = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    urano = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)
    neptuno = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)


    yang.position[:] = position_yang
    yang.color[:] = color_yang
    yin.position[:] = position_yin
    yin.color[:] = color_yin
    sol.position[:] = position_sol
    sol.color[:] = color_sol


    mercurio.color[:] = color_mercurio
    venus.color[:] = color_venus
    tierra.color[:] = color_tierra
    marte.color[:] = color_marte
    jupiter.color[:] = color_jupiter
    saturno.color[:] = color_saturno
    anillos.color[:] = color_anillos
    urano.color[:] = color_unranus
    neptuno.color[:] = color_neptuno


    @window.event
    def on_draw():
        glClearColor(0.1, 0.1, 0.1, 0.0)
        with pipeline:
            yang.draw(GL_TRIANGLES)
            yin.draw(GL_TRIANGLES)
            sol.draw(GL_TRIANGLES)

            mercurio.draw(GL_TRIANGLES)
            venus.draw(GL_TRIANGLES)
            tierra.draw(GL_TRIANGLES)
            marte.draw(GL_TRIANGLES)
            jupiter.draw(GL_TRIANGLES)

            anillos.draw(GL_TRIANGLES)
            saturno.draw(GL_TRIANGLES)

            urano.draw(GL_TRIANGLES)
            neptuno.draw(GL_TRIANGLES)



    @window.event
    def update(dt):
        global time
        mercurio.position[:] = position_mercurio
        venus.position[:] = position_venus
        tierra.position[:] = position_tierra
        marte.position[:] = position_marte
        jupiter.position[:] = position_jupiter
        saturno.position[:] = position_saturno
        anillos.position[:] = position_anillos
        neptuno.position[:] = position_nepturno
        urano.position[:] = position_unranus
        #time = time**dt

    update(dt = 1/60)
    pyglet.app.run()

    
