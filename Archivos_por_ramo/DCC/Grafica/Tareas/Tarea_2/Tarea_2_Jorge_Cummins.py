'''
=======================================================================================================================
    Tarea 2: Modelación y Computación Gráfica para Ingenieros (CC3501-1)
-----------------------------------------------------------------------------------------------------------------------
    Autor: Jorge Cummins
    Rut: 21353175-1
    Fecha de Redaccion: 11 de Septiembre de 2024
    Fecha Limite de Entrega: 13 de Septiembre de 2024
-----------------------------------------------------------------------------------------------------------------------
    Palabras Previas:
    Este archivo (hasta el momento en que se envia) contiene los codigos utilizados para la implementacion de la tarea
    2 de la asignatura de Modelación y Computación Gráfica para Ingenieros. Esta fue dividida en diferentes secciones
    para intentar mejorar su comprension. Ademas, se intento incluir la mayor cantidad de comentarios posibles para
    explicar que se intentaba realizar. En caso de cualquier sugerencia que pueda hacer mas simple la correccion o
    de manera general es bien recibida.

    A la hora de realizar esta tarea fue de gran relevancia el material entregado por el equipo docente, de esta forma
    se agradece este material que sirvio de fundamento para el desarrollo de la tarea, donde implementaciones como
    la clase "Model", "Camara" y la funcion "models_from_file" fueron adaptaciones de las otorgadas por el equipo
    docente. Tambien, si bien se realizo en un documento aparte, se tomo como inspiracion el template otorgado por los
    profesores.

    La realizacion de esta tarea conto con la implementacion de objetos externos, todos provenientes de la pagina
    "sketcfab", comunidad que se encarga del desarrollo y distribucion de, entre diferentes productos, objetos para
    modelacion (.obj). Se incorporo al final del documento las referencias respectivas a cada uno de los objetos.
=======================================================================================================================
'''
# Seccion 1: importamos paquetes ######################################################################################
#######################################################################################################################
# numpys
import numpy as np
from numpy._core.multiarray import dtype

# Variantes de pyglet
import pyglet
from pyglet.gl import *
from pyglet.math import Mat4, Vec3, clamp
from pyglet.window import Window, key
from pyglet.graphics.shader import Shader, ShaderProgram

# Resto de imports
import grafica.transformations as tr
import trimesh as tm
import os
import sys
sys.path.append(os.path.dirname((os.path.dirname(__file__))))


# Seccion 2: configuracion ############################################################################################
#######################################################################################################################
class Controller(Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.time = 0.0
        self.fov = 90
        super().set_exclusive_mouse(True)

# Configurar la ventana.
WIDTH = 800
HEIGHT = 600
window = Controller(WIDTH, HEIGHT, "Tarea 2")

# Configurar los contorles.
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
window.set_exclusive_mouse(True)


# Seccion 3: definimos las clases y funciones que se usaran ###########################################################
#######################################################################################################################
# Funcion para insertar los valores de los colores en vez de normalizarlos .
def real_rgb(r, g, b):
    return r / 255, g / 255, b / 255


# Clase para la nave.
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
        self.direction = np.zeros(2)
        self.front = np.array([0, 0, -1], dtype=np.float32)
        self.up = np.array([0, 1, 0], dtype=np.float32)
        self._buffer = pipeline.vertex_list_indexed(size, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def update(self, dt):
        self.front[0] = np.cos(self.yaw) * np.cos(self.pitch)
        self.front[1] = np.sin(self.pitch) # z?
        self.front[2] = np.sin(self.yaw) * np.cos(self.pitch)
        self.front /= np.linalg.norm(self.front)
        dir = self.direction[0]*self.front + self.direction[1]*np.cross(self.up, self.front)
        dir_norm = np.linalg.norm(dir)
        if dir_norm:
            dir /= dir_norm
        self.position += dir*self.speed*dt

    def model(self):
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0] + self.pitch, Vec3(1, 0, 0)).rotate(self.rotation[1] + self.yaw, Vec3(0, 1, 0)).rotate(self.rotation[2], Vec3(0, 0, 1))
        scale = Mat4.from_scale(Vec3(*self.scale))
        return translation @ rotation @ scale

    def draw(self):
        self._buffer.draw(GL_TRIANGLES)


# Clase para la camara.
class Camara:
    def __init__(self, x, y, z, speed=1) -> None:
        self.position = np.array([x, y, z], dtype=np.float32)
        self.yaw = 0
        self.pitch = 0
        self.speed = speed
        self.sensitivity = 0.01
        self.front = np.array([1, 0, -1], dtype=np.float32)
        self.up = np.array([0, 1, 0], dtype=np.float32)
        self.direction = np.zeros(2)

    def update(self, dt):
        self.front[0] = np.cos(self.yaw) * np.cos(self.pitch)
        self.front[1] = np.sin(self.pitch)
        self.front[2] = np.sin(self.yaw) * np.cos(self.pitch)
        self.front /= np.linalg.norm(self.front)
        dir = self.direction[0] * self.front + self.direction[1] * np.cross(self.up, self.front)
        dir_norm = np.linalg.norm(dir)
        if dir_norm:
            dir /= dir_norm
        self.position += dir * self.speed * dt

    def view(self):
        return Mat4.look_at(Vec3(*self.position), Vec3(*(self.position + self.front)), Vec3(*self.up))


# Clase para los modelos, es decir, para los objetos que se implementan.
class Model:
    def __init__(self, size, vertices, indices, pipeline) -> None:
        self.color = np.zeros(3, dtype=np.float32)
        self.position = np.zeros(3, dtype=np.float32)
        self.scale = np.ones(3, dtype=np.float32)
        self.rotation = np.zeros(3, dtype=np.float32)
        self._buffer = pipeline.vertex_list_indexed(size, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def model(self):
        translation = Mat4.from_translation(Vec3(*self.position))
        rotation = Mat4.from_rotation(self.rotation[0], Vec3(1, 0, 0)).rotate(self.rotation[1], Vec3(0, 1, 0)).rotate(
            self.rotation[2] , Vec3(0, 0, 1))
        scale = Mat4.from_scale(Vec3(*self.scale))
        return translation @ rotation @ scale

    def draw(self):
        self._buffer.draw(GL_TRIANGLES)


# Funcion para cargar los modelos desde un archivo, estos son en formato .obj (objetos).
def models_from_file(path, pipeline, clase, speed):
    geom = tm.load(path)
    meshes = []
    if isinstance(geom, tm.Scene):
        for m in geom.geometry.values():
            meshes.append(m)
    else:
        meshes = [geom]
    models = []
    if clase == "model":
        for m in meshes:
            m.apply_scale(2.0 / m.scale)
            m.apply_translation([-m.centroid[0], 0, -m.centroid[2]])
            vlist = tm.rendering.mesh_to_vertexlist(m)
            models.append(Model(vlist[0], vlist[4][1], vlist[3], pipeline))
    elif clase == "ship":
        for m in meshes:
            m.apply_scale(2.0 / m.scale)
            m.apply_translation([-m.centroid[0], 0, -m.centroid[2]])
            vlist = tm.rendering.mesh_to_vertexlist(m)
            models.append(Ship(vlist[0], vlist[4][1], vlist[3], speed, pipeline))
    return models


if __name__ == "__main__":
    vsource = """
#version 330
in vec3 position;
in vec3 color;

uniform mat4 transform;
uniform mat4 model;
uniform mat4 projection = mat4(1.0);
uniform mat4 view = mat4(1.0);

out vec3 fragColor;

void main() {
    fragColor = color;
    gl_Position = projection * view * model * vec4(position, 1.0f);
}
    """

    fsource = """
#version 330
in vec3 fragColor;

uniform vec3 color;

out vec4 outColor;

void main() {
    outColor = vec4(color, 1.0f);
}
  """

    pipeline = ShaderProgram(Shader(vsource, "vertex"), Shader(fsource, "fragment"))

    # Camara
    cam = Camara(0, 2, 0, 5)

    # Objetos que se usaran
    # Configuracion del sol
    sol = models_from_file("objects/sun.obj", pipeline, "model", 0)[0]
    sol.color = real_rgb(255, 255, 0)
    sol.scale = [1.5]*3
    sol.position = [0, 0, 0]

    # Configuracion planetas
    # Planeta 1
    planet_1 = models_from_file("objects/planet.obj", pipeline, "model", 0)[0]
    planet_1.color = real_rgb(30, 50, 120)
    planet_1.scale = [.3] * 3
    planet_1.position = [4, 0, 4]

    # Planeta 2
    planet_2 = models_from_file("objects/craneo.obj", pipeline, "model", 0)[0]
    planet_2.color = real_rgb(220, 220, 220)
    planet_2.scale = [.5] * 3
    planet_2.position = [8, 0, 8]

    # Planeta 3
    planet_3 = models_from_file("objects/New rojoooect.obj", pipeline, "model", 0)[0]
    planet_3.color = real_rgb(80, 80, 80)
    planet_3.scale = [1] * 3
    planet_3.position = [11, 0, 11]

    # Planeta 4
    planet_4 = models_from_file("objects/skipper.obj", pipeline, "model", 0)[0]
    planet_4.color = real_rgb(150, 42, 50)
    planet_4.scale = [0.4] * 3
    planet_4.position = [13, 0, 13]


    # Extras
    nae = models_from_file("objects/ImageToStl.com_untitled8.obj", pipeline, "ship", speed = 5)[0]
    nae.color = real_rgb(150, 140, 150)
    nae.scale = [.5] * 3
    nae.position = [2, 1, 0]
    nae.rotation = [-np.pi/2, 0, -np.pi-3*np.pi/2]


    # Bonus: luna, en este, este caso, del planeta 2
    planet_2_moon = models_from_file("objects/planet.obj", pipeline, "model", 0)[0]
    planet_2_moon.color = real_rgb(70, 150, 80)
    planet_2_moon.scale = [.1] * 3
    planet_2_moon.position = [planet_2.position[0]+0.5, planet_2.position[1]+0.5, planet_2.position[2]+0.5]


    # Escena
    scene = [sol, planet_1, planet_2, planet_3, planet_4, nae, planet_2_moon]



    @window.event
    def on_draw():
        window.clear()
        glClearColor(0.1, 0.1, 0.1, 0.0)
        glEnable(GL_DEPTH_TEST)
        pipeline.use()
        with pipeline:
            pipeline["view"] = cam.view()
            pipeline["projection"] = Mat4.perspective_projection(window.aspect_ratio, 1, 10, window.fov)
            pipeline["color"] = nae.color
            pipeline["model"] = nae.model()
            for m in scene:
                pipeline["color"] = m.color
                pipeline["model"] = m.model()
                m.draw()

    @window.event
    def update(dt):
        dtheta = window.time

        planet_1.position = [4*np.cos(0.2*dtheta), 0, 4*np.sin(0.2*dtheta)]
        planet_1.rotation = [0, 0.5*dtheta, 0]

        planet_2.position = [8*np.cos(0.1*dtheta), 0, 4*np.sin(0.1*dtheta)]
        planet_2.rotation = [0, 0.2*dtheta, 0]

        planet_3.position = [11*np.cos(-0.05*dtheta), -np.pi/7, 11*np.sin(-0.05*dtheta)]
        planet_3.rotation = [0, -0.3*dtheta, 0]

        planet_4.position = [13*np.cos(0.15 * dtheta), 0, 13*np.sin(0.15 * dtheta)]
        planet_4.rotation = [0, 0.3 * dtheta, 0]


        planet_2_moon.position = [8*np.cos(0.1*dtheta)-0.5*np.cos(0.5*dtheta), 0, 4*np.sin(0.1*dtheta)-0.5*np.sin(0.5*dtheta)]
        planet_2_moon.rotation = [0, 1.2*dtheta, 0]


        window.time += dt
        cam.update(dt)
        nae.update(dt)


    # Pa ponerle weno a la maquina
    # Volante de la nae (Mover el mouse)
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        nae.yaw += dy * nae.sensitivity # += PARA QUE FUNCIONE
        nae.pitch += dx * nae.sensitivity   # += PARA QUE FUNCIONE
        nae.pitch = clamp(nae.pitch, -(np.pi /4), np.pi / 4)  # = PARA QUE FUNCIONE



    # Meterle shala a la maquina (Presionar tecla)
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.W:
            nae.direction[0] = 1
        if symbol == key.S:
            nae.direction[0] = -1
        if symbol == key.A:
            nae.direction[1] = 1
        if symbol == key.D:
            nae.direction[1] = -1



    # To' duro (Soltar la tecla)
    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == key.W or symbol == key.S:
            nae.direction[0] = 0
        if symbol == key.A or symbol == key.D:
            nae.direction[1] = 0



    # Manejar to' volao (Scroll del mouse)
    @window.event
    def on_mouse_scroll(x, y, scroll_x, scroll_y):
        window.fov += scroll_y * .5
        window.fov = clamp(window.fov, 10, 90)



    pyglet.clock.schedule_interval(update, 1 / 60)  # Uno aqui arrogante con 165Hz en su monitor principal
    pyglet.app.run()


