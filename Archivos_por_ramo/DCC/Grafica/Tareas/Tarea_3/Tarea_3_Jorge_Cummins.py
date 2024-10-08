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
''' Funcion real_rgb()

Funcion para insertar los colores en vez de normalizarlos.
El objetivo de esta funcion es tomar los valores de RGB originales [0, 255] y normalizarlos a [0, 1].
Fue para insertar los colores sin tener la necesidad de normalizarlos en cada instante.

int int int -> float float float
'''
def real_rgb(r, g, b):
    return r/255, g/255, b/255



''' Funcion generate_ring()

Funcion para generar anillos de un astro. Esta funcion venia con el template original.
'''
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


''' Funcion create_sphere()
Funcion que, inspirada en la funcion create_ring, crea una
esfera discretizando en coordenadas esfericas phi y theta.

Recibe "definition" que corresponde a la cantidad de divisiones y devuelve Model para crear la esfera.
'''
def create_sphere(definition):
    # Coordenadas de posicion (posiciones) para una esfera
    positions = np.zeros((definition * definition) * 3, dtype=np.float32)
    # Coordenadas de texturas (uv), texturas aun no implementadas
    uv = np.zeros((definition * definition) * 2, dtype=np.float32)
    # Arreglo de indices
    indices = np.zeros((6 * (definition ) * (definition)), dtype=np.int32)

    dtheta = 2 * np.pi / definition  # Angulo theta
    dphi = np.pi / (definition - 1)  # Angulo phi

    r = 1  # radio, seteado a 1

    # Generar posiciones y coordenadas de texturas....aun (creo) no lo implemento
    for i in range(definition):
        for j in range(definition):
            idx = 3 * (i * definition + j)
            tidx = 2 * (i * definition + j)

            theta = j * dtheta  # Desplazamos por theta
            phi = i * dphi      # Desplazamos por phi
            
            # Llenamos una lista con coordenadas tanto de posicion como de texturas, esto en coordenadas esfericas
            positions[idx:idx+3] = [r * np.sin(phi) * np.cos(theta), r * np.sin(phi) * np.sin(theta),r * np.cos(phi)]
            uv[tidx:tidx+2] = [j / (definition - 1), i / (definition - 1)]

    # Generar indices de triangulos, originalmente era hasta definition-1, pero se cambio a definition para cerrar la esfera
    idx = 0
    for i in range(definition ):
        for j in range(definition ):

            # Triángulos que forman la malla, al igual que para las texturas pero esta vez para la forma
            indices[idx:idx+3] = [i * definition + j,
                                  i * definition + j+1,
                                  i * definition + j+definition]
            indices[idx+3:idx+6] = [i * definition + j+1,
                                    i * definition + j+definition+1,
                                    i * definition + j+definition]
            idx += 6

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
in vec2 texCoords;

uniform mat4 u_model;
uniform mat4 u_view = mat4(1.0);
uniform mat4 u_projection = mat4(1.0);

out vec2 fragTexCoords;

void main() {
    gl_Position = u_projection * u_view * u_model * vec4(position, 1.0f);
    fragTexCoords = texCoords;    
}
    """
    frag_source = """
#version 330
in vec2 fragTexCoords;

out vec4 outColor;

uniform sampler2D u_texture;

void main() {
    outColor = texture(u_texture, fragTexCoords);
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
    sphere = create_sphere(36) # Si es que parece un pacman es porque no tuve tiempo de arreglarla
    sphere.init_gpu_data(pipeline)

    ring = generate_ring(36)
    ring.init_gpu_data(pipeline)

    world.add_node("sun_to_root")
    world.add_node("sun_base", attach_to="sun_to_root", mesh=sphere, pipeline=pipeline, scale=[2.0, 2.0, 2.0])

    # Mercurio
    world.add_node("mercury_to_sun", attach_to="sun_to_root")
    world.add_node("mercury_base", attach_to="mercury_to_sun", mesh=sphere, pipeline=pipeline, scale=[.1, .1, .1], position=[5,0,0])

    # Venus
    world.add_node("venus_to_sun", attach_to="sun_to_root")
    world.add_node("venus_base", attach_to="venus_to_sun", mesh=sphere, pipeline=pipeline, scale=[.4, .4, .4], position=[8,0,0])

    # Tierra
    world.add_node("earth_to_sun", attach_to="sun_to_root")
    world.add_node("earth_base", attach_to="earth_to_sun", mesh=sphere, pipeline=pipeline, scale=[.43, .43, .43], position=[9,0,0])
    
    # Marte
    world.add_node("mars_to_sun", attach_to="sun_to_root")
    world.add_node("mars_base", attach_to="mars_to_sun", mesh=sphere, pipeline=pipeline, scale=[.25, .25, .25], position=[12,0,0])

    # Jupiter
    world.add_node("jupiter_to_sun", attach_to="sun_to_root")
    world.add_node("jupiter_base", attach_to="jupiter_to_sun", mesh=sphere, pipeline=pipeline, scale=[.9, 0.9, 0.9], position=[15,0,0])

    # Saturno -> Anillo
    world.add_node("saturn_to_sun", attach_to="sun_to_root")
    world.add_node("saturn_base",attach_to="saturn_to_sun", mesh=sphere, pipeline=pipeline, scale=[.8, .8, .8], position=[18,0,0])
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
        world["earth_to_sun"]["rotation"][1] = window.time
        world["mars_to_sun"]["rotation"][1] = window.time
        world["jupiter_to_sun"]["rotation"][1] = window.time
        world["venus_to_sun"]["rotation"][1] = -window.time
        world["mercury_to_sun"]["rotation"][1] = window.time

        world.update()
        cam.update()
        window.time+=dt

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()
