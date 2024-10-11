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
    Este archivo contiene el desarrollo realizado para la tarea 3 de la asignatura Modelacion y Computacion Grafica para
    Ingenieros (CC3501-1). Al igual que en entregas posteriores, la tarea fue subdividia en secciones para intentar
    facilitar la comprension tanto por quien revise como por quien realiza la tarea (es dcir, yo).

    Fue de gran relevancia para la realizacion las clases auxiliares y catedras para cumplir (o intentar) los
    requisitos. Ademas, en una copia del template otorgado por el cuerpo docente (este archivo) fue realizado evitando
    alterar lo que ya se incorporaba, donde ademas se adjunto el template original.

    Para realizar esta tarea se utilizo un objeto externo que presentara su respectiva referencia al final del
    documento. Para el momento en que fue entregada, ningun documento aparte se tiene registro de haber sido modificado,
    el unico cambio transcendental fue extraer archivos de sus carpetas/directorios originales para evitar problemas
    con las rutas de los archivos.
=========================================================================================================================
"""
# Seccion 1: importamos librerias ########################################################################################
###########################################################################################################################
# Librerias utilizadas
import pyglet
from networkx.lazy_imports import attach
from pyglet.gl import *
from pyglet.graphics.shader import Shader, ShaderProgram
import numpy as np

# Librerias del cuerpo docente
from grafica.scene_graph import SceneGraph
from grafica.camera import OrbitCamera
from grafica.helpers import mesh_from_file
from grafica.drawables import Model, Texture
from pyglet.window import Window, key

# Seccion 2: configuracion ################################################################################################
###########################################################################################################################
class Controller(Window):
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

    dphi = 2 * np.pi / (definition-1)  # Definimos Phi theta (entre el plano OXY y OZ)
    dtheta = np.pi / (definition-1)  # Definimos angulo Phi (entre r y OZ)

    r = 1.0  # Radio de la esfera

    # Generar posiciones de vértices y coordenadas de texturas (UV)
    for i in range(definition):
        for j in range(definition):
            idx = 3 * (i * definition + j)
            tidx = 2 * (i * definition + j)

            theta = i * dtheta  # Ángulo azimutal
            phi = j * dphi      # Ángulo polar

            positions[idx:idx+3] = [-r * np.sin(theta) * np.cos(phi), -r * np.sin(theta) * np.sin(phi),-r * np.cos(theta)]
            uv[tidx:tidx+2] = [j / (definition), i / (definition )]

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


    return Model(positions, uv, None, indices)


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

    pipeline = ShaderProgram(Shader(
        vert_source, "vertex"),
        Shader(frag_source, "fragment"))

    # Camara
    cam1 = OrbitCamera(10)
    cam1.width = 800
    cam1.height = 800
    
    cam2 = OrbitCamera(5)
    cam2.width = 800
    cam2.height = 800

    cam3 = OrbitCamera(5)
    cam3.width = 800
    cam3.height = 800
    
    cam4 = OrbitCamera(5)
    cam4.width = 800
    cam4.height = 800
    
    cam5 = OrbitCamera(5)
    cam5.width = 800
    cam5.height = 800


    cam = cam1

    # Ventana/control
    window = Controller(cam.width, cam.height, "Tarea 3")
    window.set_exclusive_mouse(True)


    # Creamos los objetos sin textura
    # Esfera
    sphere = create_sphere(36)
    sphere.init_gpu_data(pipeline)
    # Anillo
    ring = generate_ring(36)
    ring.init_gpu_data(pipeline)
    # Nave, Si, es la estrella de la muerte y el mejor modelo con una textura que pudiera implementar, creditos
    # respectivos al final del documento
    no_i_am_your_father = mesh_from_file("assets/death_star.obj")[0]["mesh"]
    no_i_am_your_father.init_gpu_data(pipeline)

    '''
    Iniciamos el grafo
    '''
    world = SceneGraph(cam)

    # Sol
    world.add_node("sun_to_root")

    world.add_node("sun_base",
                   attach_to="sun_to_root",
                   mesh=sphere,
                   pipeline=pipeline,
                   position=[0,0,0],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/sun.jpg"))

    # Mercurio
    world.add_node("mercury_to_sun",
                   attach_to="sun_to_root")

    world.add_node("mercury_base",
                   attach_to="mercury_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.14, .14, .14],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/mercury.jpg"))

    # Venus
    world.add_node("venus_to_sun",
                   attach_to="sun_to_root")

    world.add_node("venus_base",
                   attach_to="venus_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.4, .4, .4],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/venus.jpg"))

    # Tierra
    world.add_node("earth_to_sun",
                   attach_to="sun_to_root")

    world.add_node("earth_base",
                   attach_to="earth_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.43, .43, .43],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/earth.jpg"))

    world.add_node("moon_to_earth",
                   attach_to = "earth_base")

    world.add_node("moon_base",
                   attach_to= "moon_to_earth",
                   mesh = sphere,
                   pipeline = pipeline,
                   scale = [0.2, 0.2, 0.2],
                   rotation = [np.pi*3/2, -np.pi/2, np.pi],
                   texture = Texture("assets/moon.jpg"))

    # Marte
    world.add_node("mars_to_sun",
                   attach_to="sun_to_root")

    world.add_node("mars_base",
                   attach_to="mars_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.25, .25, .25],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/mars.jpg"))

    # Nave
    world.add_node("nave_to_mars",
                   attach_to="mars_base")
    
    world.add_node("nave_base",
                   attach_to="nave_to_mars",
                   mesh=no_i_am_your_father,
                   pipeline=pipeline,
                   scale=[0.7, 0.7, 0.7],
                   texture = Texture("assets/deathstar_(1).jpg"))

    # Jupiter
    world.add_node("jupiter_to_sun",
                   attach_to="sun_to_root")

    world.add_node("jupiter_base",
                   attach_to="jupiter_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.95, 0.95, 0.95],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/jupiter.jpg"))

    # Saturno -> Anillo
    world.add_node("saturn_to_sun",
                   attach_to="sun_to_root")

    world.add_node("saturn_base",
                   attach_to="saturn_to_sun",
                   mesh=sphere,
                   pipeline=pipeline,
                   scale=[.8, .8, .8],
                   rotation=[-np.pi/2, 0, 0],
                   texture=Texture("assets/saturn.jpg"))

    world.add_node("saturn_ring",
                   attach_to="saturn_base")
    world.add_node("ring_base",
                   attach_to="saturn_ring",
                   mesh=ring,
                   pipeline=pipeline,
                   scale=[2, 2, 2],
                   rotation=[0, 0, 0],
                   cull_face=False,
                   texture=Texture("assets/saturn_ring.png"))

    # Centro del centro de rotacion binario.
    world.add_node("Liu_Cixin",
                   attach_to="sun_to_root")

    world.add_node("Liu_Cixin_base",
                   attach_to = "Liu_Cixin")

    # Urano
    world.add_node("uranus_to_centre",
                   attach_to="Liu_Cixin_base")

    world.add_node("uranus_base",
                   attach_to="uranus_to_centre",
                   mesh = sphere,
                   pipeline=pipeline,
                   scale=[0.65, 0.65, 0.65],
                   rotation=[0, 0, 0],
                   texture=Texture("assets/uranus.jpg"))
    # Neptune
    world.add_node("neptune_to_centre",
                   attach_to = "Liu_Cixin_base")

    world.add_node("neptune_base",
                   attach_to = "neptune_to_centre",
                   mesh = sphere,
                   pipeline = pipeline,
                   scale = [0.62, 0.62, 0.62],
                   rotation=[0, 0, 0],
                   texture = Texture("assets/neptune.jpg"))

    # agregar fondo estrellado con textura stars.jpg. QUITAR, es porque se ve cool.
    world.add_node("stars",
                   mesh=sphere,
                   pipeline=pipeline,
                   texture=Texture("assets/stars.jpg"),
                   scale=[50, 50, 50],
                   cull_face=False)

    # Dibujamos
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

    # Mouse
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        # Modificamos la camara segun el movimento del mouse
        cam.phi += dx * 0.001
        cam.theta += dy * 0.001
        cam1.phi = cam.phi
        cam1.theta = cam.theta
        cam2.phi += dx*0.001
        cam2.theta += dy*0.001
        cam3.phi += dx*0.001
        cam3.theta += dy*0.001
        cam4.phi += dx*0.001
        cam4.theta += dy*0.001
        cam5.phi += dx * 0.001
        cam5.theta += dy * 0.001


    # Teclado
    @window.event
    def on_key_press(symbol, modifiers):
        # Si se presiona espacio, la camara se centra en el sol con una proyeccion ortografica y orbitandolo
        if symbol == key.SPACE:
            world.camera = cam1
        
        # Si se presiona T, la camara con una proyeccion de perspectiva que esta orbitando centrada en la tierra
        if symbol == key.T:
            world.camera = cam2
        
        # Caso analogo para saturno pero con tecla S
        if symbol == key.S:
            world.camera = cam3
        
        # Caso analogo para el el centro de orbita entre neptuno y urano al presionar U
        if symbol == key.U:
            world.camera  = cam4

        # Caso analogo (por ahora) para la nave de marte
        if symbol == key.M:
            world.camera = cam5

    # Update de la escena
    def update(dt):
        domega = window.time/2
        domega_ax = window.time


        # Sol.
        world["sun_base"]["scale"] = [2.5+0.1*np.cos(domega), 2.5+0.1*np.cos(domega), 2.5+0.1*np.cos(domega)]
        world["sun_base"]["rotation"][1] = -(1/8)*domega_ax
        cam1.focus = world["sun_base"]["position"]
        cam1.position = world["sun_base"]["position"]+np.array([1, 1, 1])

        # Mercurio.
        world["mercury_base"]["rotation"][1] = (2/8)*domega_ax
        world["mercury_base"]["position"] = [(6.24+0.5*np.cos(domega))*np.cos(domega_ax), 0, (6.24+0.5*np.cos(domega))*np.sin(domega_ax)]

        # Venus.
        world["venus_base"]["rotation"][1] = -(1/8)*domega_ax
        world["venus_base"]["position"] = [(10.38+0.5*np.sin(domega))*np.cos(-0.73*window.time), 0, (10.38+0.5*np.sin(domega))*np.sin(-0.73*window.time)]

        # Tierra.
        world["earth_base"]["rotation"][1] = (4/8)*domega_ax
        world["earth_base"]["position"] = [16.19*np.cos(0.62*window.time), 0,  16.19*np.sin(0.62*window.time)]
        cam2.focus = world["earth_base"]["position"]
        cam2.position = world["earth_base"]["position"]+np.array([1, 1, 1])

        # Luna.
        world["moon_base"]["rotation"][0] = (1/16)*domega_ax
        world["moon_base"]["position"] = [1.8*np.cos(window.time), 1.8*np.sin(window.time),0]

        # Marte.
        world["mars_base"]["rotation"][1] = (3/8)*domega_ax
        world["mars_base"]["position"] = [19.44 * np.cos(0.502*window.time), 0, 19.44 * np.sin(0.502*window.time)]

        cam5.focus = world["mars_base"]["position"]
        cam5.position = world["mars_base"]["position"]+np.array([0.3, 0.3, 0.3])

        # Nave.
        world["nave_base"]["rotation"][1] = (1/8)*domega_ax
        world["nave_base"]["position"] = [1.8 * np.cos(0.502*window.time), 1.8*np.cos(window.time)*np.sin(window.time), 1.8 * np.sin(0.502*window.time)]

        # Jupiter.
        world["jupiter_base"]["rotation"][1] = domega_ax
        world["jupiter_base"]["position"] = [25.14*np.cos(0.27*window.time), 0, 25.14*np.sin(0.27*window.time)]

        # Saturno.
        world["saturn_base"]["rotation"][1] = (7/8)*domega_ax
        world["saturn_base"]["position"] = [32.09*np.cos(0.2*window.time), 0, 32.09*np.sin(0.2*window.time)]
        world["saturn_ring"]["rotation"][2] = (7/8)*domega_ax
        cam3.focus = world["saturn_base"]["position"]
        cam3.position = world["saturn_base"]["position"]+np.array([2, 2, 2])

        # Rotacion del centro comun de rotacion binaria en torno al sol.
        world["Liu_Cixin_base"]["position"] = [36.74*np.cos(0.12*window.time), 0, 36.74*np.sin(0.12*window.time)]
        cam4.focus = world["Liu_Cixin_base"]["position"]
        cam4.position = world["Liu_Cixin_base"]["position"]+np.array([6, 6, 1])

        # Urano.
        world["uranus_base"]["rotation"][2] = -(6/8)*domega_ax
        world["uranus_base"]["position"] = [3.17*np.cos(0.22*window.time+np.pi), 0, 3.17*np.sin(0.22*window.time+np.pi)]

        # Neptuno
        world["neptune_base"]["rotation"][1] = (5/8)*domega_ax
        world["neptune_base"]["position"] = [5.62*np.cos(-0.20*window.time), 0, 5.62*np.sin(-0.20*window.time)]

        world.update()
        cam.update()
        cam1.update()
        cam2.update()
        cam3.update()
        cam4.update()
        cam5.update()
        window.time+=dt

    pyglet.clock.schedule_interval(update, 1/165)
    pyglet.app.run()
