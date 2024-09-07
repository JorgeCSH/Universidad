'''
Tarea nº2
Información del trabajo:
Autor: Jorge Cummins
RUT: 21353175-1
Curso: CC3501-1
Profesor: Ivan Sipiran
Fecha: 13 de septiembre de 2024
'''

# Seccion 1: importación de librerías y configuracion ventana #########################################################
#######################################################################################################################
import trimesh as tm
import pyglet
import numpy as np
from pyglet.gl import *
import os
import sys
sys.path.append(os.path.dirname((os.path.dirname(__file__))))
import grafica.transformations as tr
from pyglet.math import Mat4, Vec3
from Archivos%20por%ramo.DCC.Grafica.Tareas.Tarea_2 import shapes


WIDTH = 1000
HEIGHT = 1000


# Seccion 2: clases utilizadas ########################################################################################
#######################################################################################################################
#Controller
class Controller(pyglet.window.Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.time = 0.0
        self.fov = 90

window = Controller(WIDTH, HEIGHT, "Tarea 2")


#Para los contorles
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
window.set_exclusive_mouse(True)


#Defina aquí una clase "Ship" para la nave
class Ship:
    pass


#Defina aquí una clase "Camara"
class Camara():
    pass


#Defina aquí una clase "Model" para el resto de los objetos
class Model():
    def __init__(self, vertices, indices, pipeline) -> None:
        self.pipeline = pipeline

        self._buffer = pipeline.vertex_list_indexed(len(vertices) // 3, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def draw(self, mode):
        self._buffer.draw(mode)


# Seccion 3:  #########################################################################################################
#######################################################################################################################
#shaders
if __name__ == "__main__":
    
    vertex_source = """
#version 330

in vec3 position;
in vec3 color;


uniform mat4 transform;
uniform mat4 view = mat4(1.0);
uniform mat4 projection = mat4(1.0);

out vec3 fragColor;

void main() {
    fragColor = color;
    gl_Position = projection * view * transform * vec4(position, 1.0f);
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
    #Creación del pipeline
    vert_program = pyglet.graphics.shader.Shader(vertex_source, "vertex")
    frag_program = pyglet.graphics.shader.Shader(fragment_source, "fragment")
    pipeline = pyglet.graphics.shader.ShaderProgram(vert_program, frag_program)

    #Defina sus objetos y la cámara
    
    

    @window.event
    def on_draw():

        glClearColor(0.1, 0.1, 0.1, 0.0)
        
        window.clear()

        pipeline.use()

       #Dibuje sus objetos


    
    def update(dt):
        #Pasa el tiempo
        window.time += dt

        #Actualice la posición de la cámara
    
        #Actualice los planetas para que giren

        
    #Control mouse
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        pass

        
    @window.event
    def on_key_press(symbol, modifiers):
        pass

    @window.event
    def on_key_release(symbol, modifiers):
        pass


    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()


