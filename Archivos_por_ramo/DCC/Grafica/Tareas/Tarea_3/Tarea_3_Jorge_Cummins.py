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
from grafica.drawables import Model, Texture


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
''' Funcion generate_ring()
Funcion para generar anillos de un astro. Esta funcion venia con el template original. 
Entrega la geometria de la esfera tanto para la malla como para las texturas, donde uv = (u, v) corresponden a las
texturas.
'''
def generate_ring(definition, texture_file=None):
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
   
    #Completamos el anillo
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
    # Coordenadas de posición (posiciones) para una esfera
    positions = np.zeros((definition * definition) * 3, dtype=np.float32)
    # Coordenadas de texturas (uv)
    uv = np.zeros((definition * definition) * 2, dtype=np.float32)
    # Índices para formar los triángulos
    indices = np.zeros((6 * (definition ) * (definition)), dtype=np.int32)

    dtheta = 2 * np.pi / definition  # Resolución azimutal
    dphi = np.pi / (definition - 1)  # Resolución polar

    r = -1.0  # Radio de la esfera

    # Generar posiciones de vértices y coordenadas de texturas (UV)
    for i in range(definition):
        for j in range(definition):
            idx = 3 * (i * definition + j)
            tidx = 2 * (i * definition + j)

            theta = j * dtheta  # Ángulo azimutal
            phi = i * dphi      # Ángulo polar

            positions[idx:idx+3] = [r * np.sin(phi) * np.cos(theta), r * np.sin(phi) * np.sin(theta),r * np.cos(phi)]
            uv[tidx:tidx+2] = [j / (definition -1), i / (definition -1)]

    # Generar índices de triángulos
    idx = 0
    for i in range(definition-1):
        for j in range(definition):

            # Triángulos que forman la malla
            indices[idx:idx+3] = [i * definition + j,
                                  i * definition + j+1,
                                  i * definition + j+definition]
            indices[idx+3:idx+6] = [i * definition + j+1,
                                    i * definition + j+definition+1,
                                    i * definition + j+definition]
            idx += 6
    
    # Para las normales
    normals = np.zeros((definition * definition) * 3, dtype=np.float32)
    for i in range(definition):
        for j in range(definition):
            idx = 3 * (i * definition + j)
            theta = j * dtheta
            phi = i * dphi
            normals[idx:idx+3] = [np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]

    return Model(positions, uv, normals, indices)


# Seccion 4: Configuracion de la escena ###############################################################################
#######################################################################################################################
'''
Configuracion de los Shaders
'''
if __name__ == "__main__":
    vert_source = """
#version 330
in vec3 position;
in vec2 texCoord;

uniform mat4 u_model;
uniform mat4 u_view = mat4(1.0);
uniform mat4 u_projection = mat4(1.0);

out vec2 fragTexCoord;

void main() { 
    gl_Position = u_projection * u_view * u_model * vec4(position, 1.0f);
    fragTexCoord = texCoord;    
}
    """
    frag_source = """
#version 330
in vec2 fragTexCoord;

out vec4 outColor;

uniform sampler2D u_texture;

void main() {
    outColor = texture(u_texture, fragTexCoord);
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
   
    #epic_sphere = mesh_from_file("assets/world.obj")
    #epic_sphere.init_gpu_data(pipeline)

    ring = generate_ring(36)
    ring.init_gpu_data(pipeline)

    omega = 2*np.pi/8

    world.add_node("sun_to_root")
    world.add_node("sun_base",
                   attach_to="sun_to_root",
                   mesh=sphere,
                   pipeline=pipeline,
                   position=[0,0,0],
                   rotation=[np.pi/2, 0, 0],
                   scale=[2.5, 2.5, 2.5],
                   texture=Texture("assets/sun.jpg"))

    # Mercurio
    world.add_node("mercury_to_sun",
                   attach_to="sun_to_root")
    world.add_node("mercury_base",
                   attach_to="mercury_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.1, .1, .1],
                   position=[5,0,0],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/mercury.jpg"))

    # Venus
    world.add_node("venus_to_sun",
                   attach_to="sun_to_root")
    world.add_node("venus_base",
                   attach_to="venus_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.4, .4, .4],
                   position=[8.5*np.cos(omega), 0, 8.5*np.sin(omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/venus.jpg"))

    # Tierra
    world.add_node("earth_to_sun",
                   attach_to="sun_to_root")
    world.add_node("earth_base",
                   attach_to="earth_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.43, .43, .43],
                   position=[11.93*np.cos(2*omega), 0,  11.93*np.sin(2*omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/earth.jpg"))
    
    # Marte
    world.add_node("mars_to_sun",
                   attach_to="sun_to_root")
    world.add_node("mars_base",
                   attach_to="mars_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.25, .25, .25],
                   position=[15.18*np.cos(3*omega), 0, 15.18*np.sin(3*omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/mars.jpg"))

    # Jupiter
    world.add_node("jupiter_to_sun",
                   attach_to="sun_to_root")
    world.add_node("jupiter_base",
                   attach_to="jupiter_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.95, 0.95, 0.95],
                   position=[20.03*np.cos(4*omega), 0, 20.03*np.sin(4*omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/jupiter.jpg"))

    # Saturno -> Anillo
    world.add_node("saturn_to_sun",
                   attach_to="sun_to_root")
    world.add_node("saturn_base",
                   attach_to="saturn_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.8, .8, .8],
                   position=[24.78*np.cos(5*omega),0, 24.78*np.sin(5*omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/saturn.jpg"))
    world.add_node("saturn_ring",
                   attach_to="saturn_base",
                   mesh=ring,
                   pipeline=pipeline,
                   scale=[2, 2, 2],
                   rotation=[0, 0, 0], cull_face=False,
                   texture=Texture("assets/saturn_ring.png"))

    # Centro del centro de rotacion binario.
    world.add_node("Liu_Cixin",
                   attach_to="sun_to_root")
    world.add_node("Liu_Cixin_base",
                   attach_to = "Liu_Cixin",
                   position=[32*np.cos(6*omega), 0, 32*np.sin(6*omega)])

    # Urano
    world.add_node("uranus_to_centre",
                   attach_to="Liu_Cixin_base")
    world.add_node("uranus_base",
                   attach_to="uranus_to_centre",
                   mesh = sphere,
                   pipeline=pipeline,
                   scale=[0.65, 0.65, 0.65],
                   position=[3.17*np.cos(7*omega), 0, 3.17*np.sin(7*omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture=Texture("assets/uranus.jpg"))
    # Neptune
    world.add_node("neptune_to_centre",
                   attach_to = "Liu_Cixin_base")
    world.add_node("neptune_base",
                   attach_to = "neptune_to_centre",
                   mesh = sphere,
                   pipeline = pipeline,
                   scale = [0.62, 0.62, 0.62],
                   position = [5.62*np.cos(8*omega), 0, 5.62*np.sin(8*omega)],
                   rotation=[np.pi/2, 0, 0],
                   texture = Texture("assets/neptune.jpg"))


    # Dibujamos
    @window.event
    def on_draw():
        window.clear()
        glClearColor(.1,.1,.1,1)

        # 3D
        glEnable(GL_DEPTH_TEST)
        # Transparencia
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable( GL_BLEND )
        with pipeline:
            world.draw()
        glDisable(GL_DEPTH_TEST)

    # Mouse
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        # Modificamos la camara segun el movimento del mouse
        cam.phi += dx * 0.001
        cam.theta += dy * 0.001
    
    # Teclado
    @window.event
    def on_key_press(symbol, modifiers):
        pass

    # Update de la escena 
    def update(dt):
        dif = window.time
#        world["sun_base"]["scale"][0:3] = [2.5+0*0.1*np.cos(dif), 2.5+0*0.1*np.cos(dif), 2.5+0*0.1*np.cos(dif)]
        world["mercury_to_sun"]["rotation"][1] = window.time
        world["venus_to_sun"]["rotation"][1] = -0.73*window.time
        world["earth_to_sun"]["rotation"][1] = 0.62*window.time
        world["mars_to_sun"]["rotation"][1] = 0.502*window.time
        world["jupiter_to_sun"]["rotation"][1] = 0.27*window.time
        world["saturn_to_sun"]["rotation"][1] = 0.2*window.time
        world["Liu_Cixin"]["rotation"][1] = 0.12*window.time
        world["uranus_to_centre"]["rotation"][1] = 0.22*window.time
        world["neptune_to_centre"]["rotation"][1] = -0.20*window.time

        world.update()
        cam.update()
        window.time+=dt

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()
