"""
=======================================================================================================================
    Tarea 2: Modelación y Computación Gráfica para Ingenieros (CC3501-1)
-----------------------------------------------------------------------------------------------------------------------
    Autor: Jorge Cummins
    Rut: 21353175-1
    Fecha de Redaccion: 11 de Septiembre de 2024
    Fecha Limite de Entrega: 13 de Septiembre de 2024
    Fecha en que se Entrego: 15 de Septiembre de 2024 (atraso autorizado)
-----------------------------------------------------------------------------------------------------------------------
    Palabras Previas:
    Este archivo (hasta el momento en que se envia) contiene los codigos utilizados para la implementacion de la tarea
    2 de la asignatura de Modelación y Computación Gráfica para Ingenieros. Esta fue dividida en diferentes secciones
    para intentar mejorar su comprension. Ademas, se intento incluir la mayor cantidad de comentarios posibles para
    explicar que se intentaba realizar. En caso de cualquier sugerencia que pueda hacer mas simple la correccion o
    de manera general es bien recibida.

    A la hora de realizar esta tarea fue de gran relevancia el material entregado por el equipo docente, de esta forma
    se agradece este material que sirvio de fundamento para el desarrollo de la tarea, donde se implementaron clases
    como la clase "Model", "Camara" y la funcion "models_from_file" fueron adaptaciones de las otorgadas por el equipo
    docente. Tambien, si bien se realizo en un documento aparte, se tomo como inspiracion el template otorgado por los
    profesores.

    La realizacion de esta tarea conto con la implementacion de objetos externos, todos provenientes de la pagina
    "sketcfab", comunidad que se desarrolladores y distribuidores de, entre diferentes productos, objetos para
    modelacion (.obj).
=======================================================================================================================
"""
# Seccion 1: importamos librerias #####################################################################################
#######################################################################################################################
# numpys.
import numpy as np
from OpenGL.raw.GLU import gluLookAt
from numpy._core.multiarray import dtype

# Pyglet y sus variantes, no necesariamente se utilizan todas.
import pyglet
from pyglet.gl import *
from pyglet.math import Mat4, Vec3, clamp
from pyglet.window import Window, key
from pyglet.graphics.shader import Shader, ShaderProgram

# Misc.
import grafica.transformations as tr
import trimesh as tm
import os
import sys
sys.path.append(os.path.dirname((os.path.dirname(__file__))))


# Seccion 2: configuracion ############################################################################################
#######################################################################################################################
'''
Clase "Controller" 
Esta clase se encarga de controlar la ventana, es la encargada de manejar los eventos de la ventana, como el dibujo.
Es la que fue entregada por el cuerpo docente
'''
class Controller(Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.time = 0.0
        self.fov = 90


# Configurar la ventana, tambien la que fue entregada por el cuerpo docente con las mismas dimensiones.
WIDTH = 1000
HEIGHT = 1000
window = Controller(WIDTH, HEIGHT, "Tarea 2")

# Configurar los contorles.
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
window.set_exclusive_mouse(True)


# Seccion 3: definimos las clases y funciones que se usaran ###########################################################
#######################################################################################################################
'''
Funcion para insertar los valores de los colores en vez de normalizarlos.
El objetivo de esta funcion es tomar los valores de RGB originales [0, 255] y normalizarlos a [0, 1].
Fue para insertar los colores sin tener la necesidad de normalizarlos en cada instante.
Toma los valores asociados a RGB y devuelve una tupla normalizada.
'''
def real_rgb(r, g, b):
    return r / 255, g / 255, b / 255

'''
Clase "Ship" 
Clase que se encarga de contener todos los atributos de la nave.
Para su creacion se tomo como inspiracion la clase "Camera" de la clase auxiliar 4.
'''
class Ship:
    def __init__(self, size, vertices, indices, speed, pipeline) -> None:
        self.color = np.zeros(3, dtype=np.float32)
        self.position = np.zeros(3, dtype=np.float32)
        self.scale = np.ones(3, dtype=np.float32)
        self.rotation = np.zeros(3, dtype=np.float32)
        self.sensitivity = 0.001
        self.yaw = 0
        self.pitch = 0
        self.speed = speed
        self.direction = 0
        self.front = np.zeros(3, dtype=np.float32)
        self.up = np.array([0, 1, 0], dtype=np.float32)
        self._buffer = pipeline.vertex_list_indexed(size, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def update(self, dt):
        # Update la parte delantera (vector front)
        self.front[0] = np.cos(self.yaw) * np.cos(self.pitch)
        self.front[1] = np.sin(self.pitch)
        self.front[2] = np.sin(self.yaw) * np.cos(self.pitch)
        self.front /= np.linalg.norm(self.front)
        # Moviemiento basado en direccion de la nave
        self.position += self.direction * self.front* self.speed*dt

    def model(self):
        # Montamos matriz de transformacion
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0], Vec3(1, 0, 0)).rotate(self.rotation[1], Vec3(0, 1, 0)).rotate(self.rotation[2], Vec3(0, 0, 1))
        scale = Mat4.from_scale(Vec3(*self.scale))
        return translation @ rotation @ scale

    def draw(self):
        self._buffer.draw(GL_TRIANGLES)


'''
Clase camara
Clase que se encarga de tener todos los atributos de la camara.
Calcula la posicion de la camara de tal manera que sigue al objeto que se le entregue
'''
class Camara():
    # Inicializamos los atributos
    def __init__(self, target) -> None:
        self.target = target # objeto que queremos seguir
        self.position = np.zeros(3, dtype=np.float32)
        self.up = np.zeros(3, dtype=np.float32)
        self.forward = np.zeros(3, dtype=np.float32)

    # Actualizar la camara
    def update(self, dt):
        self.position = self.target.position - self.target.front + self.target.up
        # Calculamos el vector forward y el vector up
        self.forward = self.target.position - self.position
        self.forward /= np.linalg.norm(self.forward)

        self.up = np.cross(np.cross(self.forward, self.target.up), self.forward)

    def view(self):
        return Mat4.look_at(Vec3(*self.position), Vec3(*(self.position + self.forward)), Vec3(*self.up))


'''
Clase Model

Clase que se encarga de contener todos los atributos de los objetos que seran utilizados en la escena que no son 
la nave.

Fue hecha en base a la utilizada y creada en la clase por el auxiliar (auxiliar numero 4).
'''
class Model():
    # Inicializamos los atributos
    def __init__(self, size, vertices, indices, pipeline) -> None:
        self.color = np.zeros(3, dtype=np.float32)
        self.position = np.zeros(3, dtype=np.float32)
        self.scale = np.ones(3, dtype=np.float32)
        self.rotation = np.zeros(3, dtype=np.float32)
        self._buffer = pipeline.vertex_list_indexed(size, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    # Montamos la matriz de transformacion
    def model(self):
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0], Vec3(1, 0, 0)).rotate(self.rotation[1], Vec3(0, 1, 0)).rotate(
            self.rotation[2] , Vec3(0, 0, 1))
        scale = Mat4.from_scale(Vec3(*self.scale))
        return translation @ rotation @ scale

    # Dibujamos el objeto
    def draw(self):
        self._buffer.draw(GL_TRIANGLES)



'''
Funcion models_from_file.

Al igual que la clase model, fue usada en clase auxiliar y permite, en base a un "path" (o direccion) de un objeto, 
cargarlo seleccionando en "clase" si corresponde a algun modelo o una nave que se movera con una rapidez "speed". 
'''
def models_from_file(path, clase, speed, pipeline):
    geom = tm.load(path)
    meshes = []
    if isinstance(geom, tm.Scene):
        for m in geom.geometry.values():
            meshes.append(m)
    else:
        meshes = [geom]
    models = []
    # Dependiendo de la clase, se creara un objeto u otro.
    # En caso de ser "model", se creara un objeto de la clase "Model"
    if clase == "model":
        for m in meshes:
            m.apply_scale(2.0 / m.scale)
            m.apply_translation([-m.centroid[0], 0, -m.centroid[2]])
            vlist = tm.rendering.mesh_to_vertexlist(m)
            models.append(Model(vlist[0], vlist[4][1], vlist[3], pipeline))
    # En caso de ser "ship", se creara un objeto de la clase "Ship"
    elif clase == "ship":
        for m in meshes:
            m.apply_scale(2.0 / m.scale)
            m.apply_translation([-m.centroid[0], 0, -m.centroid[2]])
            vlist = tm.rendering.mesh_to_vertexlist(m)
            models.append(Ship(vlist[0], vlist[4][1], vlist[3], speed, pipeline))
    return models


# Seccion 4: Configuracion de la escena ###############################################################################
#######################################################################################################################
'''
Configuracion de los Shaders
'''
if __name__ == "__main__":
    vertex_source = """
#version 330
in vec3 position;
in vec3 color;

uniform mat4 transform;
uniform mat4 view = mat4(1.0);
uniform mat4 projection = mat4(1.0);
uniform mat4 model;

out vec3 fragColor;

void main() {
    fragColor = color;
    gl_Position = projection * view * model * vec4(position, 1.0f);
}
    """

    fragment_source = """
#version 330

in vec3 fragColor;

uniform vec3 color;

out vec4 outColor;

void main() {
    outColor = vec4(color, 1.0f);
}
  """

    # Aca creamos el pipeline con los shaders
    vert_program = pyglet.graphics.shader.Shader(vertex_source, "vertex")
    frag_program = pyglet.graphics.shader.Shader(fragment_source, "fragment")
    pipeline = pyglet.graphics.shader.ShaderProgram(vert_program, frag_program)


    # Aca van los objetos que se van a usar en la escena
    # Cargamos la nave usando un modelo de la comunidad de Sketchfab.
    Spacecraft = models_from_file("objects/UFO.obj", "ship", 5, pipeline)[0] # Similar al resto de objetos, solo que ahora se usa "Ship" y se le otorga una velocidad diferente de 0.
    Spacecraft.color = real_rgb(150, 140, 150)
    Spacecraft.scale = [0.5] * 3
    Spacecraft.position = [4, 0, 4]

    # Configuramos el sol.
    sol = models_from_file("objects/sun.obj", "model", 0, pipeline)[0]  # Cargamos el path y creamos usando "Model".
    sol.color = real_rgb(255, 255, 0)                                            # Le damos color usando la funcion "real_rgb" para normalizarla.
    sol.scale = [1.5]*3                                                                   # Escalamos el sol.
    sol.position = [0, 0, 0]                                                              # Posicion, lo situamos en el origen

    # Configuracion planetas
    # Planeta 1, el mas cercano al sol, usamos el modelo 3D dado por el cuerpo docente.
    planet_1 = models_from_file("objects/planet.obj", "model", 0, pipeline)[0]
    planet_1.color = real_rgb(30, 50, 120)
    planet_1.scale = [0.3] * 3
    planet_1.position = [4+sol.position[0], 0, 4+sol.position[2]]

    # Planeta 2, segundo mas cercano al sol, usamos un modelo de la comunidad de Sketchfab.
    planet_2 = models_from_file("objects/Skull.obj", "model", 0, pipeline)[0]
    planet_2.color = real_rgb(220, 220, 220)
    planet_2.scale = [0.5] * 3
    planet_2.position = [8+sol.position[0], 0, 8+sol.position[0]]

    # Planeta 3, tercer planeta, usamos un modelo de la comunidad de Sketchfab.
    planet_3 = models_from_file("objects/Moai.obj", "model", 0, pipeline)[0]
    planet_3.color = real_rgb(80, 80, 80)
    planet_3.scale = [1] * 3
    planet_3.position = [11+sol.position[0], 0, 11+sol.position[0]]

    # Planeta 4, planeta mas alejado del sol, usamos un modelo de la comunidad de Sketchfab.
    planet_4 = models_from_file("objects/skipper.obj", "model", 0, pipeline)[0]
    planet_4.color = real_rgb(150, 42, 50)
    planet_4.scale = [0.4] * 3
    planet_4.position = [13+sol.position[0], 0, 13+sol.position[1]]


    # Extra
    # Bonus: luna para un planeta, en este, este caso, del planeta 2. Se usa el objeto entregado por el cuerpo docente
    planet_2_moon = models_from_file("objects/planet.obj", "model", 0, pipeline)[0]
    planet_2_moon.color = real_rgb(70, 150, 80)
    planet_2_moon.scale = [.1] * 3
    planet_2_moon.position = [planet_2.position[0]+0.5+sol.position[0], planet_2.position[1]+0.5, planet_2.position[2]+0.5+sol.position[0]]


    # En una lista metemos todos los objetos que se usaran en la escena.
    scene = [sol, planet_1, planet_2, planet_3, planet_4, planet_2_moon]


    # Cargamos la camara, recibe como parametro la nave/objeto que quiere seguir.
    cam = Camara(Spacecraft)


    # Dibjuamos en la ventana
    @window.event
    def on_draw():

        glClearColor(0.1, 0.1, 0.1, 0.0)

        glEnable(GL_DEPTH_TEST)

        window.clear()

        pipeline.use()

        # Camara
        pipeline["view"] = cam.view()
        pipeline["projection"] = Mat4.perspective_projection(WIDTH/HEIGHT, 0.1, 10, window.fov)

        # Nave
        pipeline["color"] = Spacecraft.color
        pipeline["model"] = Spacecraft.model()
        Spacecraft.draw()


        # Objetos de la escena
        for m in scene:
            pipeline["color"] = m.color
            pipeline["model"] = m.model()
            m.draw()

    @window.event
    def update(dt):
        # Pasa el tiempo
        window.time += dt
        dtheta = window.time # Reduntante pero es por costumbre jeje

        #Actualice la posición de la cámara
        Spacecraft.update(dt)
        cam.update(dt)

        #Actualice los planetas para que giren
        # Posicion y rotacion planeta 1
        planet_1.position = [4*np.cos(0.2*dtheta), 0, 4*np.sin(0.2*dtheta)]
        planet_1.rotation = [0, 0.5*dtheta, 0]

        # Planeta 2
        planet_2.position = [8*np.cos(0.1*dtheta), 0, 4*np.sin(0.1*dtheta)]
        planet_2.rotation = [0, 0.2*dtheta, 0]

        #Planeta 3
        planet_3.position = [11*np.cos(-0.05*dtheta), -np.pi/7, 11*np.sin(-0.05*dtheta)]
        planet_3.rotation = [0, -0.3*dtheta, 0]

        #Planeta 4
        planet_4.position = [13*np.cos(0.15 * dtheta), 0, 13*np.sin(0.15 * dtheta)]
        planet_4.rotation = [0, 0.3 * dtheta, 0]


        # Luna del planeta 2
        planet_2_moon.position = [8*np.cos(0.1*dtheta)-0.5*np.cos(0.5*dtheta), 0, 4*np.sin(0.1*dtheta)-0.5*np.sin(0.5*dtheta)]
        planet_2_moon.rotation = [0, 1.2*dtheta, 0]

        # Movimiento del mouse...la pase mal con esto...
        Spacecraft.rotation = [0, -Spacecraft.yaw, np.sin(Spacecraft.pitch)]



    # Movimiento del mouse.
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        Spacecraft.yaw += dx * Spacecraft.sensitivity
        Spacecraft.pitch += dy * Spacecraft.sensitivity
        Spacecraft.pitch = clamp(Spacecraft.pitch, -(np.pi /4), np.pi / 4)


    # Presionar tecla W o S, no se especifico A y D por ende para evitar complicaciones se decidio omitir.
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.W:
            Spacecraft.direction = 1
        if symbol == key.S:
            Spacecraft.direction = -1


    # Soltar tecla W o S.
    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == key.W or symbol == key.S:
            Spacecraft.direction = 0


    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()


"""
=======================================================================================================================
Links de donde se sacaron los modelos:
- Sol: Entregado por el cuerpo docente
- Nave: https://sketchfab.com/3d-models/ufo-by-jeroen-2a3256decde84d9c9aa42704c1293126
- Planeta 1: Entregado por el cuerpo docente
- Planeta 2: https://sketchfab.com/3d-models/calavera-a04a252f8376401bad417f0d9f263b2a
- Planeta 3: https://sketchfab.com/3d-models/chicken-gun-moai-24807e56e7df4fbd882bb9f9f98b9ba3
- Planeta 4: https://sketchfab.com/3d-models/skipper-eb3db0d0e67944c2b80a16a1b3b78ea7
- Luna: Entregado por el cuerpo docente

Como ejecutar (o ejecute) la tarea:
La tarea fue ejecutada en dos condiciones que para tener referencia fueron:
- Windows 11, python3.12, IDLE: Pycharm, grafica.transformations segun mostrado en catedra y ejecutado con la opcion
  de ejecutar del IDLE.
- Debian 12, python, Neovim, grafica.transformations segun mostrado en catedra y ejecutado desde la terminal.
Todo esto despues de haber seguido las instrucciones de setup en el repositorio, esto para windows version pip y 
Linux.
=======================================================================================================================
"""