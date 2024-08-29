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



    position_yang, color_yang = crear_planeta(0, 0, 1, 1, 1, 0.32)
    position_yin, color_yin = crear_planeta(0, 0, 0, 0, 0, 0.319)

    position_sol, color_sol = crear_planeta(0, 0, 1, 1, 0, 0.15)
    position_mercurio, color_mercurio = crear_planeta(-.2-0.007, 0, 66/255, 43/255, 1/255, 0.007)
    position_venus, color_venus = crear_planeta(-0.25-0.015, 0, 215/255, 141/255, 1/255, 0.015)
    position_tierra, color_tierra = crear_planeta(-0.3-0.02, 0, 0, 1, 0, 0.016)
    position_marte, color_marte = crear_planeta(-0.35-0.01, 0, 1, 0, 0, 0.01)
    position_jupiter, color_jupiter = crear_planeta(-0.5-0.05, 0, 255/255, 147/255, 0/255, 0.05)
    position_saturno, color_saturno = crear_planeta(-0.7-0.027, 0, 233/255, 108/255, 0/255, 0.025)
    position_anillos, color_anillos = crear_planeta(-0.7-0.027, 0, 96/255, 96/255, 96/255, 0.048)
    position_unranus, color_unranus = crear_planeta(-0.82-0.018, 0, 123/255, 163/255, 254/255, 0.02)
    position_nepturno, color_neptuno = crear_planeta(-0.9-0.017, 0, 0, 0, 1, 0.017)



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

    
