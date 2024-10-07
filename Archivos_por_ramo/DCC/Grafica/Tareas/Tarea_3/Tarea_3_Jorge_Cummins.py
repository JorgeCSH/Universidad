"""
=========================================================================================================================
    Tarea 3: Modelacion y Computacion Grafica para Ingenieros (CC3501-1)
------------------------------------------------------------------------------------------------------------------------
    Autor: Jorge Cummins
    Rut: 21.353.175-1
    Fecha de Redaccion: 06 de Octubre de 2024
    Fecha Limite de Entrega: 04 de Octubre de 2024
    Fecha en que se Entrego: 
------------------------------------------------------------------------------------------------------------------------
    Palabras Previas:


=========================================================================================================================
"""
# Seccion 1: importamos librerias ########################################################################################
########################################################################################################################### 
# Librerias utilizadas
import pyglet
from pyglet.gl import *
from pyglet.graphics.shader import Shader, ShaderProgram
import numpy as np

# Librerias del cuerpo docente
from grafica.scene_graph import SceneGraph
from grafica.camera import OrbitCamera
from grafica.helpers import mesh_from_file
from grafica.drawables import Model


# Seccion 2: configuracion ################################################################################################
###########################################################################################################################

class Controller(pyglet.window.Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.time = 0
        self.focus = "sun_base"
        self.sensitivity = 0.1


# Seccion 3: definimos las clases y funciones que se usaran ###############################################################
###########################################################################################################################
'''
Funcion para insertar los colores en vez de normalizarlos.
El objetivo de esta funcion es tomar los valores de RGB originales [0, 255] y normalizarlos a [0, 1].
Fue para insertar los colores sin tener la necesidad de normalizarlos en cada instante.

int int int -> float float float
'''
def real_rgb(r, g, b):
    return r/255, g/255, b/255



def generate_ring(definition):
    # coordenadas de posición
    positions = np.zeros((definition)*3*2, dtype=np.float32) 
    # coordenadas de texturas
    uv = np.zeros((definition)*2*2, dtype=np.float32)
    dtheta = 2*np.pi / definition
    r1 = 0.5
    r2 = 1.0

    for i in range(definition):
        idx = 3*i
        tidx = 2*i
        theta = i*dtheta
        positions[idx:idx+3] = [np.cos(theta)*r2, np.sin(theta)*r2, 0.0]
        if i%2==0:
            uv[tidx:tidx+2] = [1, 1]
        else:
            uv[tidx:tidx+2] = [1, 0]

    for i in range(definition):
        idx = 3*(i+definition)
        tidx = 2*(i+definition)
        theta = i*dtheta
        positions[idx:idx+3] = [np.cos(theta)*r1, np.sin(theta)*r1, 0.0]
        if i%2==0:
            uv[tidx:tidx+2] = [0, 1]
        else:
            uv[tidx:tidx+2] = [0, 0]

    indices = np.zeros(6*definition, dtype=np.int32)
    for i in range(definition-1):
        idx = 6*i
        # t0
        indices[idx:idx+3] = [i, i+1, i+definition]
        # t1
        indices[idx+3:idx+6] = [i+1, i+definition+1, i+definition]
   
    # Completamos el anillo
    # indices[3*definition:] = [definition, definition - 1, 0]
    idx = 6*(definition-1)
    indices[idx:idx+3] = [definition-1, 0, 2*definition-1]
    indices[idx+3:idx+6] = [2*definition-1, definition, 0]

    return Model(positions, uv, None, indices)


# Seccion 4: Configuracion de la escena ###############################################################################
###########################################################################################################################
'''
Configuracion de los Shaders
'''
if __name__ == "__main__":
    vert_source = """
#version 330
in vec3 position;

uniform mat4 u_model;
uniform mat4 u_view = mat4(1.0);
uniform mat4 u_projection = mat4(1.0);

void main() {
    gl_Position = u_projection * u_view * u_model * vec4(position, 1.0f);
}
    """
    frag_source = """
#version 330

out vec4 outColor;

void main() {
    outColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}
    """

    pipeline = ShaderProgram(Shader(vert_source, "vertex"), Shader(frag_source, "fragment"))

    # Camara
    cam = OrbitCamera(10)
    cam.width = 800
    cam.height = 800
    window = Controller(cam.width, cam.height, "Tarea 3")
    window.set_exclusive_mouse(True)

    world = SceneGraph(cam)
    sphere = mesh_from_file("assets/world.obj")[0]["mesh"] # solo como referencia
    sphere.init_gpu_data(pipeline)

    ring = generate_ring(36)
    ring.init_gpu_data(pipeline)

    world.add_node("sun_to_root")
    world.add_node("sun_base", attach_to="sun_to_root", mesh=sphere, pipeline=pipeline, scale=[1.5, 1.5, 1.5])
    world.add_node("earth_to_sun", attach_to="sun_to_root")
    world.add_node("earth_base", attach_to="earth_to_sun", mesh=sphere, pipeline=pipeline, scale=[.1, .1, .1], position=[5,0,0])
    world.add_node("saturn_to_sun", attach_to="sun_to_root")
    world.add_node("saturn_base",attach_to="saturn_to_sun", mesh=sphere, pipeline=pipeline, scale=[.8, .8, .8], position=[10,0,0])
    world.add_node("saturn_ring", attach_to="saturn_base", mesh=ring, pipeline=pipeline, scale=[2, 2, 2], rotation=[np.pi/2, 0, 0], cull_face=False)
    
    @window.event
    def on_draw():
        window.clear()
        glClearColor(.1,.1,.1,1)

        # 3D
        glEnable(GL_DEPTH_TEST)
        # Transparencia
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glEnable( GL_BLEND );
        with pipeline:
            world.draw()
        glDisable(GL_DEPTH_TEST)

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        # Modificamos la camara segun el movimento del mouse
        cam.phi += dx * 0.001
        cam.theta += dy * 0.001

    @window.event
    def on_key_press(symbol, modifiers):
        pass

    def update(dt):
        world["saturn_to_sun"]["rotation"][1] = window.time
        world["earth_to_sun"]["rotation"][1] = -window.time
        world.update()
        cam.update()
        window.time+=dt

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()
