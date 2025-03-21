"""
========================================================================================================================
    Tarea 4: Modelacion y Computacion Grafica para Ingenieros (CC3501-1)
------------------------------------------------------------------------------------------------------------------------
    Autor: Jorge Cummins
    Rut: 21.353.175-1
    Fecha de Redaccion: 01 de Noviembre de 2024
    Fecha Limite de Entrega: 25 de Octubre de 2024
    Fecha en que se Entrego: 04 de Noviembre de 2024 (se autorizaron atrasos, fecha limite final)
------------------------------------------------------------------------------------------------------------------------
Palabras Previas:

=========================================================================================================================
"""
# Librerias de python
from pyglet.window import Window, key
from pyglet.gl import *
from pyglet.app import run
from pyglet import math
from pyglet import clock
import trimesh as tm
import sys, os
import numpy as np

#Librerias del curso
sys.path.append(os.path.dirname(os.path.dirname((os.path.dirname(__file__)))))
from utils.helpers import mesh_from_file, init_pipeline
from utils.camera import FreeCamera
from utils.scene_graph import SceneGraph
from utils.drawables import Texture, PointLight, DirectionalLight, SpotLight, Material

class Controller(Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.time = 0

class MyCam(FreeCamera):
    def __init__(self, position=np.array([0, 0, 0]), camera_type="perspective"):
        super().__init__(position, camera_type)
        self.direction = np.array([0,0,0])
        self.speed = 2

    def time_update(self, dt):
        self.update()
        dir = self.direction[0]*self.forward + self.direction[1]*self.right
        dir_norm = np.linalg.norm(dir)
        if dir_norm:
            dir /= dir_norm
        self.position += dir*self.speed*dt
        self.focus = self.position + self.forward

def models_from_file(path, pipeline):
    geom = tm.load(path)
    meshes = []
    if isinstance(geom, tm.Scene):
        for m in geom.geometry.values():
            meshes.append(m)
    else:
        meshes = [geom]

    models = []
    for m in meshes:
        m.apply_scale(2.0 / m.scale)
        m.apply_translation([-m.centroid[0], 0, -m.centroid[2]])
        vlist = tm.rendering.mesh_to_vertexlist(m)
        models.append(Model(vlist[4][1], vlist[3], pipeline))

    return models

class Model:
    def __init__(self, vertices, indices, pipeline) -> None:
        self.pipeline = pipeline
        
        self._buffer = pipeline.vertex_list_indexed(len(vertices)//3, GL_TRIANGLES, indices)
        self._buffer.position = vertices

    def draw(self, mode):
        self._buffer.draw(mode)

if __name__ == "__main__":

    #Controller / window
    controller = Controller(800,600,"Tarea 4")
    controller.set_exclusive_mouse(True)

    #Cámara
    cam = MyCam([0,2,2])

    #Para localizar archivos, fijese como se usa en el pipeline de ejemplo
    root = os.path.dirname(__file__)

    # Ejemplo de pipeline, con el clásico Phong shader visto en clases
    phong_pipeline = init_pipeline(root + "/basic.vert", root + "/phong.frag")


    # Pipelines que voy creando, pro ahora comentados para que no me fundan la grafica
    color_pipeline = init_pipeline(root + "/basic.vert", root + "/color.frag")
    # flat_pipeline = init_pipeline(root + "/flat.vert", root + "/flat.frag")
    # phong_pipeline = init_pipeline(root + "/color_mesh_lit.vert", root + "/phong.frag")
    # toon_pipeline = init_pipeline(root + "/basic.vert", root + "/toon.frag")
    # textured_pipeline = init_pipeline(root + "/basic.vert", root + "/phong.frag")
    

    #grafo para contener la escena    
    world = SceneGraph(cam)
    
    #luz de ejemplo
    world.add_node("luz ejemplo",
                   light=PointLight(),
                   pipeline=color_pipeline,
                   rotation=[np.pi/2, 0, 0],
                   position=[0, -1, 0])

    #Nave para navegar su escena
    #realmente es solo decorativa :D
    nave = mesh_from_file(root +"/nave.obj")[0]["mesh"]
    world.add_node("nave", 
                   mesh=nave,
                   pipeline=color_pipeline,
                   rotation=[0, np.pi/2*0, 0],
                   material=Material())

    planeta_provisional = mesh_from_file(root+ "/sphere.obj")[0]["mesh"]
    world.add_node("planeta_provisional",
                   mesh=planeta_provisional,
                   pipeline=color_pipeline,
                   position=[0, 1, 0],
                   material=Material(ambient = [1.0, 0.0, 0.0], diffuse=[1.0, 0.0, 0.0], shininess=50))


    @controller.event
    def on_draw():
        controller.clear()
        glClearColor(0.1, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)

        world.draw()

    @controller.event
    def on_key_press(symbol, modifiers):
        if symbol == key.SPACE: controller.light_mode = not controller.light_mode
        if symbol == key.W:
            cam.direction[0] = 1
        if symbol == key.S:
            cam.direction[0] = -1

        if symbol == key.A:
            cam.direction[1] = 1
        if symbol == key.D:
            cam.direction[1] = -1


    @controller.event
    def on_key_release(symbol, modifiers):
        if symbol == key.W or symbol == key.S:
            cam.direction[0] = 0

        if symbol == key.A or symbol == key.D:
            cam.direction[1] = 0

    @controller.event
    def on_mouse_motion(x, y, dx, dy):
        cam.yaw += dx * .001
        cam.pitch += dy * .001
        cam.pitch = math.clamp(cam.pitch, -(np.pi/2 - 0.01), np.pi/2 - 0.01)

        world["nave"]["rotation"] = [0, -cam.yaw, cam.pitch]


    @controller.event
    def on_mouse_scroll(x, y, scroll_x, scroll_y):
        controller.light_distance += scroll_y*.01

    def update(dt):
        world.update()
        cam.time_update(dt)

        world["nave"]["position"] = cam.position + cam.forward*2 + [0, -1.5, 0]

        #======== Movimiento de planetas no lo olvide!! ============


        #============================================

        world.update()

        controller.time += dt

    clock.schedule_interval(update,1/60)
    run()


"""
=======================================================================================================================
Extras:

Palabras finales:
=======================================================================================================================
"""

