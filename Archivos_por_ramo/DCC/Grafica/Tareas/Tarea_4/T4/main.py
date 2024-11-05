"""
=========================================================================================================================
 * attenuation;   Tarea 4: Modelacion y Computacion Grafica para Ingenieros (CC3501-1)
------------------------------------------------------------------------------------------------------------------------
    Autor: Jorge Cummins
    Rut: 21.353.175-1
    Fecha de Redaccion: 4 de Noviembre de 2024
    Fecha Limite de Entrega: 25 de Octubre de 2024
    Fecha en que se Entrego: 4 de Noviembre de 2024 (aceptando atrasos)
------------------------------------------------------------------------------------------------------------------------
Palabras Previas:
- El presente documento contiene los archivos solicitados con la realización de la tarea n4 del curso finalizada y 
realizada por Jorge Cummins. Este documento fue entregado en formato zip como solicitado.

- Esta tarea presenta diversos archivos en los que se destacan archivos en formato .frag y .vert, 
(o mejor dicho en lenguaje, creo, glsl) donde fueron realizados los shaders solicitados, además de un archivo main.py 
donde se encuentran el desarrollo en formato Python para la ejecución de la tarea.

- La realización, si bien fue realizada por el autor mencionado, hizo uso de material externo permitido según las
instrucciones de la tarea, donde se hizo uso de los desarrollos realizados en clase auxiliar. Además, como punto de 
partida y considerando el contexto inicial donde se contaba con uno de los documentos de shaders ya "completo", fue utilizado como
punto de partida para la realización del resto.

- Los desarrollos de la tarea no se vieron sin errores, estos se encuentran detallados tanto en algunos de los archivos
de los shaders al final de estos y más explicito al final de este presente documento en la sección de palabras finales.
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
        self.speed = 6

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


# Funcion hecha por mi para no normalizar manualmente los colores
def rgb(r, g, b):
    return [r/255, g/255, b/255]



if __name__ == "__main__":

    #Controller / window
    controller = Controller(800,600,"Tarea 4")
    controller.set_exclusive_mouse(True)

    #Cámara
    cam = MyCam([0,8,25])

    #Para localizar archivos, fijese como se usa en el pipeline de ejemplo
    root = os.path.dirname(__file__)

    # Pipelines que se usaran.....ESTE LO IMPLEMENTE YO
    color_pipeline = init_pipeline(root + "/basic.vert", root + "/color.frag")
    flat_pipeline = init_pipeline(root + "/flat.vert", root + "/flat.frag")
    phong_pipeline = init_pipeline(root + "/basic.vert", root + "/phong.frag")
    toon_pipeline = init_pipeline(root + "/basic.vert", root + "/toon.frag")
    textured_pipeline = init_pipeline(root + "/basic.vert", root + "/textured.frag")
    multi_pipeline = [color_pipeline, flat_pipeline, phong_pipeline, toon_pipeline, textured_pipeline]

    # Cargamos los modelos
    planet = mesh_from_file(root + "/sphere.obj")[0]["mesh"]
    nave = mesh_from_file(root + "/nave.obj")[0]["mesh"]
   
    #grafo para contener la escena    
    world = SceneGraph(cam)

    # Creamos los objetos/grafo de la escena
    # Nodo general, inicialmente con las luces.
    world.add_node("god_node")

    # PointLight que sale del sol
    world.add_node("sun_light",
                   attach_to="god_node",
                   light=PointLight(),
                   pipeline=multi_pipeline, 
                   position=[0, 0, 0]
                   )

    # DirectionalLight, este se busco que apunte de arriba hacia abajo
    world.add_node("divine_light",
                   attach_to="god_node",
                   light=DirectionalLight(),
                   pipeline=multi_pipeline,
                   rotation = [-np.pi/2, 0, 0]
                   )

    # Creamos el modelo del sol
    world.add_node("sun_model",
                   attach_to="sun_light",
                   mesh=planet,
                   pipeline=color_pipeline,
                   position = [0, 0, 0],
                   scale = [5.0, 5.0, 5.0],
                   material=Material(ambient = rgb(255, 255, 0),
                                     diffuse = rgb(255, 255, 0),
                                     specular = rgb(255, 255, 0)
                                     )
                   )

    # Planeta con color shader
    world.add_node("color_planet",
                  attach_to="sun_model",
                  mesh=planet,
                  pipeline=color_pipeline,
                  scale=[0.2, 0.2, 0.2],
                  material=Material(ambient=rgb(255, 0, 0),
                                    diffuse=rgb(255, 0, 0),
                                    specular=rgb(255, 0, 0)
                                    )
                   )
    
    # Planeta con flat shader
    world.add_node("flat_planet",
                  attach_to="sun_model",
                  mesh=planet,
                  pipeline=flat_pipeline,
                  scale=[0.25, 0.25, 0.25],
                  material=Material(ambient=rgb(0, 50, 10),
                                    diffuse=rgb(0, 50, 10),
                                    specular=rgb(0, 50, 10),
                                    )
                  )

    # Planeta con phong shader
    world.add_node("phong_planet",
                  attach_to="sun_model",
                  mesh=planet,
                  pipeline=phong_pipeline,
                  scale=[0.18, 0.18, 0.18],
                  material=Material(ambient=rgb(150, 40, 150),
                                    diffuse=rgb(150, 40, 150),
                                    specular=rgb(150, 40, 150)
                                    )
                  )

    # Planeta con toon shader
    world.add_node("toon_planet",
                  attach_to="sun_model",
                  mesh=planet,
                  pipeline=toon_pipeline,
                  scale=[0.3, 0.3, 0.3],
                  material=Material(ambient=rgb(5, 5, 120),
                                    diffuse=rgb(5, 5, 120),
                                    specular=rgb(5, 5, 120)
                                    )
                  )

    # Planeta con texture shader
    world.add_node("textured_planet",
                   attach_to="sun_model",
                   mesh=planet,
                   pipeline=textured_pipeline,
                   texture=Texture("earth.jpg"),
                   scale=[0.3, 0.3, 0.3],
                   material=Material(ambient=rgb(100, 100, 100), 
                                     diffuse=rgb(100, 100, 100),
                                     )
                   )
                   

    # Nodo de la nave
    world.add_node("nave",
                   mesh=nave,
                   pipeline=phong_pipeline,
                   rotation=[0, np.pi/2, 0],
                   material=Material(ambient=rgb(130, 130, 130))
                   )
                   
    # Luz que sigue a la nave, esta un poco mas atras para que gane el efecto
    world.add_node("nave_light",
                   attach_to="nave",
                   light=PointLight(diffuse=rgb(50,25, 50)), 
                   pipeline=multi_pipeline,
                   position=[-0.1, 0.5, 0]
                   )
   
    @controller.event
    def on_draw():
        controller.clear()
        glClearColor(0.01, 0.01, 0.05, 1)
        #glClearColor(0.1, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)
        world.draw()

    @controller.event
    def on_key_press(symbol, modifiers):
        #if symbol == key.SPACE: controller.light_mode = not controller.light_mode
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
        domega = controller.time
        dtheta = domega/2

        world["nave"]["position"] = cam.position + cam.forward*2 + [0, -1.5, 0]

        #======== Movimiento de planetas no lo olvide!! ============
        # Movimiento del sol 
        world["sun_model"]["rotation"] = [0, 0, 0]
        world["sun_light"]["position"] = [0, 0, 0]
        
        # Movimiento del planeta con color shader
        world["color_planet"]["position"] = [1.2*np.cos(dtheta*1.3), 0, 1.2*np.sin(dtheta*1.3)]
        world["color_planet"]["rotation"] = [0, domega, 0]
        
        # Movimiento del planeta con flat shader
        world["flat_planet"]["position"] = [1.7*np.cos(-dtheta*0.7), 0, 1.7*np.sin(-dtheta*0.7)]
        world["flat_planet"]["rotation"] = [0, 1.1*domega, 0]
        
        # Movimiento del planeta con phong shader
        world["phong_planet"]["position"] = [2.1*np.cos(dtheta*1), 0, 2.1*np.sin(dtheta*1)]
        world["phong_planet"]["rotation"] = [0, 1*domega, 0]
        
        # Movimiento del planeta con toon shader
        world["toon_planet"]["position"] = [2.5*np.cos(dtheta*0.4), 0, 2.5*np.sin(dtheta*0.4)]
        world["toon_planet"]["rotation"] = [0, 0.8*domega, 0]
    
        # Movimiento del planeta con texture shader 
        world["textured_planet"]["position"] = [3.2*np.cos(dtheta*1.1), 0, 3.2*np.sin(dtheta*1.1)]
        world["textured_planet"]["rotation"] = [0.02*domega, -1.3*domega, 0.05*domega] 


        #============================================

        world.update()

        controller.time += dt

    clock.schedule_interval(update,1/60)
    run()


"""
=======================================================================================================================
Palabras Finales:
Comparado con realizaciones previas, aprovecharé este apartado para realizar algunos comentarios con respecto a ciertos problemas que se tuvo de extraña procedencia mientras se realizaba la tarea. Específicamente y como fue comentado en algunos de los shaders, hubo problemas a la hora de cargarlos.

El primer problema es que al momento de realizar esta tarea se trabajo en dos diferentes equipos, un computador de sobremesa (PC principal) y un laptop para los momentos en que estaba en la Universidad o fuera de mi casa. Cuando se inició el desarrollo de esta tarea, esto fue en el PC, al momento de realizarla esta arrojaba errores que se pensó eran de desarrollo. Esto llevo a una serie de problemas en especial al intentar ejecutar códigos que se suponían debían funcionar y por ende llevo a una manipulación bastante profunda (en un inicio) de los documentos de los shakers o procesos que no hicieron más que enredar o directamente que dejara de hacer funcionar la tarea. Durante los últimos dos días de desarrollo, es decir, domingo 3 de noviembre y lunes 4 de noviembre se trabajó en el laptop debido a circunstancias mayores donde me pude percatar que el problema era de mi computador, esto debido a que la versión que la branch que se cargó no era la que presentaba los intentos de arreglos de cuando realizaba los códigos en mi PC principal. Más aún, daban el resultado que se suponía deberían haber dado desde un inicio.

Si bien una gran mayoría de problemas fueron solucionados, entre los que destaca que el specular cuando no se nombraba (incluso en archivos vacíos) arrojaba error diciendo que era necesario para calcular este parámetro que supuestamente requería de él (lo cual no podría haber sido puesto a que en algunos casos ni se nombraba). Sin embargo, destaca un problema que persistió, el cual se hizo especial énfasis en los comentarios de los shaders. Este problema en cuestión correspondió a que al cargarse el phong shader (específicamente este en cualquiera de sus versiones, sé probo 2 versiones más otras 3 diferentes que eran editadas por mí para ver si lograba solucionar) en donde a menos que se le quitara el parámetro "attenuation", estos no cargaban o cargaban con una atenuación que hacía de color negro al planeta. Se pensó que era algún problema con como estaba escrito el shader, sin embargo si se cambiaba el nombre, o mejor dicho el rol de los shaders, esto tambien pasaba y la unica forma que quedo para poder intentar solucionar este problema al cual dedique dos dias y la creacion de una branch completamente nueva en mi repositorio fue eliminando la atenuacion en todos los shaders menos el phong. Esto no arroja los mejores resultados pero por lo menos permite visualizar los planetas. De igual manera se incorporo una linea de codigo comentada en todos los shader donde se tomo esta decision para poder realizar pruebas en caso de que no funcione esta version.

Para finalizar lo que pareciera ser un ensayo de problemas, me gustaría disculparme por la extensión y por no haber consultado previamente. Durante el plazo oficial no se realizo debido a falta de tiempo de la cual me hago responsable y durante el receso decidio no molestar realizando consultas.

Como se ejecuto:
Computador de sobremesa: dos opciones:
-> Windows 11 con pycharm y neovim como editores, en pycharm fue donde se ejecuto en un virtual environment creado segun las instrucciones del repositorio, en neovim solo se edito en un inicio.
-> Arch linux con editor neovim como editor, esto sourceando un environment segun las instrucciones del repositiorio oficial.

Laptop:
-> Arch linux, neovim, analogo al sistema de sobremesa.

Disculpe por los errores de ortografia, es lunes, 4 de noviembre y son las 23.55.
=======================================================================================================================
"""
