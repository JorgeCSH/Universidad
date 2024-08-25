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


    ej_position, ej_color = crear_planeta(0, .2, 0, 1, 0, .7)
    
    ej_vlist = pipeline.vertex_list(3*DEFINITION, GL_TRIANGLES)

    ej_vlist.position[:] = ej_position
    ej_vlist.color[:] = ej_color

    @window.event
    def on_draw():
        glClearColor(0.1, 0.1, 0.1, 0.0)
        with pipeline:
            ej_vlist.draw(GL_TRIANGLES)


    @window.event
    def update(dt):
        pass

    pyglet.app.run()

    
