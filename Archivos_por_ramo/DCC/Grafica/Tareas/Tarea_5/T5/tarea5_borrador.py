"""
=======================================================================================================================
    Tarea 5: Modelación y Computación Gráfica para Ingenieros (CC3501-1)
-----------------------------------------------------------------------------------------------------------------------
    Autor: Jorge Cummins
    Rut: 21353175-1
    Fecha de Redaccion: 6 de Noviembre de 2024
    Fecha Limite de Entrega: 15 de Noviembre de 2024
    Fecha en que se Entrego: 25 de Noviembre de 2024 (atraso autorizado)
-----------------------------------------------------------------------------------------------------------------------
    Palabras Previas:

=======================================================================================================================
"""

from networkx.algorithms.bipartite import collaboration_weighted_projected_graph
import numpy as np
import os
from pyglet import window, gl, app, clock
from scipy.fft import prev_fast_len

from utils.drawables import Texture, PointLight, DirectionalLight, SpotLight, Material
from utils import helpers, scene_graph, drawables, camera, drawables


class Controller(window.Window):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.input = np.zeros(3)
        self.speed = 5


class Sphere(drawables.Model):
    def __init__(self, resolution=20):
        position_data = np.zeros(6 * resolution * resolution)
        index_data = np.zeros(6 * (2 * resolution - 1) * (resolution - 1))
        normal_data = np.zeros(6 * resolution * resolution)

        delta_phi = np.pi / (resolution - 1)
        delta_theta = 2 * np.pi / (resolution - 1)

        vcount = 0
        for i in range(2 * resolution):
            for j in range(resolution):
                phi = j * delta_phi
                theta = i * delta_theta
                position_data[vcount : vcount + 3] = [
                    np.cos(theta) * np.sin(phi),
                    np.cos(phi),
                    np.sin(theta) * np.sin(phi),
                ]
                normal_data[vcount : vcount + 3] = [
                    np.cos(theta) * np.sin(phi),
                    np.cos(phi),
                    np.sin(theta) * np.sin(phi),
                ]
                vcount += 3

        icount = 0
        for i in range(2 * resolution - 1):
            for j in range(resolution - 1):
                current = i * resolution + j
                index_data[icount : icount + 3] = [
                    current + 1,
                    current,
                    current + resolution,
                ]
                index_data[icount + 3 : icount + 6] = [
                    current + resolution,
                    current + resolution + 1,
                    current + 1,
                ]
                icount += 6

        super().__init__(position_data, None, normal_data, index_data)


''' Clase Planeta
Clase donde contengo toda las caracteristicas de los planetas, ademas de algunos comportamientos como la actualizacion
de la pocision, velocidad, etc.

'''

class Planeta:
    def __init__(self, masa, radio, posicion, velocidad, id):
        self.masa = masa
        self.radio = radio
        self.posicion = posicion
        self.velocidad = velocidad
        self.id = id
        self.radio_escalar = (self.radio[0]**(2)+self.radio[1]**(2)+self.radio[2]**(2))**(1/2)

    # Metodo update_pocision, usa el metodo de newton
    def update_posicion(self, dt):
        self.posicion[0] += self.velocidad[0]*dt
        self.posicion[1] += self.velocidad[1]*dt
        self.posicion[2] += self.velocidad[2]*dt


    # Metodo update_velocidad, usa el metodo de newton
    def update_velocidad(self, m2, pos2):
        G = 6.67430*(10**(-11))
        r = ((self.posicion[0]-pos2[0])**2 + (self.posicion[1]-pos2[1])**2 + (self.posicion[2]-pos2[2])**2)**(1/2)
        F = G*(self.masa*m2)/(r**2+self.radio_escalar)
        self.velocidad[0] += F*(pos2[0]-self.posicion[0])/(r+self.radio_escalar)
        self.velocidad[1] += F*(pos2[1]-self.posicion[1])/(r+self.radio_escalar)
        self.velocidad[2] += F*(pos2[2]-self.posicion[2])/(r+self.radio_escalar)




SUN_MASS = 1000000
SUN_RADIUS = 1.0
SUN_VELOCITY = 0

if __name__ == "__main__":
    controller = Controller(1000, 1000, "Tarea 5")

    cam = camera.OrbitCamera(10, camera.Camera.ORTHOGRAPHIC)
    cam.width = controller.width
    cam.height = controller.height

    world = scene_graph.SceneGraph(cam)

    shaders_folder = os.path.join(os.path.dirname(__file__), "shaders")
    pipeline = helpers.init_pipeline(
        shaders_folder + "/color_mesh_lit.vert", shaders_folder + "/color_mesh_lit.frag"
    )
    lpipeline = helpers.init_pipeline(
        shaders_folder + "/color_mesh.vert", shaders_folder + "/color_mesh.frag"
    )

    planet_mesh = Sphere(36)

    # Nodo de la luz del sol
    world.add_node("sun_light",
                   light=PointLight(),
                   pipeline=pipeline,
                   position=[0, 0, 0]
                   )

    # Nodo del sol, esta conectado al nodo de la luz
    world.add_node(
        "sun",
        attach_to= "sun_light",
        mesh=planet_mesh,
        pipeline=lpipeline,
        scale =  [SUN_RADIUS, SUN_RADIUS, SUN_RADIUS],
        color = [1.0, 0.8, 0.3],
        position = [0, 0, 0],
    )

    # Creamos una cantidad de planetas aleatoria, entre 10 y 15
    planets_quantities = np.random.randint(10, 15)
    print(planets_quantities)

    # Creacion de los planetas
    planets_atrocities = []
    for i in range(0, planets_quantities):
        # Color del planeta
        r = np.random.rand()
        g = np.random.rand()
        b = np.random.rand()
        crayon = [r, g, b]

        # Tamaño del planeta
        planet_x = SUN_RADIUS*((planets_quantities-i)/planets_quantities)/2
        planet_y = SUN_RADIUS*((planets_quantities-i)/planets_quantities)/2
        planet_z = SUN_RADIUS*((planets_quantities-i)/planets_quantities)/2

        # Posicion del planeta
        # Decidimos de manera aleatoria en cual octante (creo que asi se llama) esta inicialmente un planeta.
        coin_flipx = np.random.choice([-1, 1], 1)
        coin_flipy = np.random.choice([-1, 1], 1)
        coin_flipz = np.random.choice([-1, 1], 1)
        # Coordenadas
        planet_coordx = 0
        planet_coordy = 0
        planet_coordz = 0
        # Coordenada inicial en el eje OX
        last_pos_x = [0.2]
        if coin_flipx == 1:
            planet_coordx = np.random.uniform(SUN_RADIUS+last_pos_x[len(last_pos_x)-1], ( SUN_RADIUS+0.2)*7)
            last_pos_x += [planet_coordx]
        last_neg_x = [-0.2]
        if coin_flipx == -1:
            planet_coordx = np.random.uniform((-SUN_RADIUS-0.2)*7, -SUN_RADIUS+last_neg_x[len(last_neg_x)-1])
            last_neg_x += [planet_coordx]
        # Coordenada inicial en el eje OY
        last_pos_y = [0.2]
        if coin_flipy == 1:
            planet_coordy = np.random.uniform(SUN_RADIUS+last_pos_y[len(last_pos_y)-1], ( SUN_RADIUS+0.2)*7)
            last_pos_y += [planet_coordy]
        last_neg_y = [-0.2]
        if coin_flipx == -1:
            planet_coordy = np.random.uniform((-SUN_RADIUS-0.2)*7, -SUN_RADIUS+last_neg_y[len(last_neg_y)-1])
            last_neg_y += [planet_coordy]
        # Coordenada inicial en el eje OZ
        last_pos_z = [0.2]
        if coin_flipz == 1:
            planet_coordz = np.random.uniform(SUN_RADIUS+last_pos_z[len(last_pos_z)-1], ( SUN_RADIUS+0.2)*7)
            last_pos_z += [planet_coordz]
        last_neg_z = [-0.2]
        if coin_flipx == -1:
            planet_coordz = np.random.uniform((-SUN_RADIUS - 0.2) * 7 , -SUN_RADIUS +last_neg_z[len(last_neg_z)-1])
            last_neg_z += [planet_coordz]

        # Velocidad inicial, vectorial
        v_x = np.random.uniform(-2, 2)
        v_y = np.random.uniform(-2, 2)
        v_z = np.random.uniform(-2, 2)

        # Juntamos todas las componentes en listas (que se interpretaran como vectores...probablemente sea mejor usar un arreglo)
        # radio inicial
        #PLANET_RADIUS = (((planet_x)**(2))+((planet_y)**(2))+((planet_z)**(2)))**(1/2)
        PLANET_RADIUS = [planet_x, planet_y, planet_z]
        # posicion inicial
        #PLANET_POS = ((PLANET_POS_VEC[0]**(2))+(PLANET_POS_VEC[1]**(2))+(PLANET_POS_VEC[2]**(2)))**(1/2)
        PLANET_POS = [planet_coordx + planet_x, planet_coordy + planet_y, planet_coordz + planet_z]
        # velocidad inicial
        #PLANET_VEL = ((v_x**(2))+(v_y**(2))+(v_z**(2)))**(1/2)
        PLANET_VEL = [v_x, v_y, v_z]
        # Masa inicial
        PLANET_MASS = np.random.randint(5000, 10000)

        # arreglo donde contemenos las clases con la info de cada planeta
        planets_atrocities += [Planeta(masa = PLANET_MASS, radio = PLANET_RADIUS, posicion = PLANET_POS, velocidad = PLANET_VEL, id = i)]

        # Nodo con cada planeta
        world.add_node(
            name = f"planet{i}",
            mesh = planet_mesh,
            pipeline = lpipeline,
            scale = PLANET_RADIUS,
            material = Material(ambient = crayon,
                                diffuse = [crayon[i]*np.random.rand() for i in range(0, len(crayon))],
                                specular = [crayon[i]*np.random.rand() for i in range(0, len(crayon))]),
            color = crayon,
        )

    # Aca creamos los planetas
    for i in range(0, planets_quantities):
        world[f"planet{i}"]["position"] = planets_atrocities[i].posicion

    @controller.event
    def on_draw():
        controller.clear()
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        world.draw()

    @controller.event
    def on_key_press(symbol, modifiers):
        if symbol == window.key.W:
            controller.input[1] = 1
        if symbol == window.key.S:
            controller.input[1] = -1

        if symbol == window.key.A:
            controller.input[0] = 1
        if symbol == window.key.D:
            controller.input[0] = -1


    @controller.event
    def on_key_release(symbol, modifiers):
        if symbol == window.key.W or symbol == window.key.S:
            controller.input[1] = 0

        if symbol == window.key.A or symbol == window.key.D:
            controller.input[0] = 0

    def update(dt):
        cam.phi += controller.input[0] * controller.speed * dt
        cam.theta += controller.input[1] * controller.speed * dt

        # Update posicion planetas dado a que se updetean las velocidades de los planetas
        for i in range(0, len(planets_atrocities)):
            planeta_afectado = planets_atrocities[i]
            # Update de velocidad dado a posicion respecto a otros planetas
            j = 0
            while j < len(planets_atrocities):
                planeta_afectante = planets_atrocities[j]
                if j == i:
                    j += 1
                planeta_afectado.update_velocidad(planeta_afectante.masa, planeta_afectante.posicion)
                j += 1
            # Update de velocidad dado a posicion respecto al sol
            planeta_afectado.update_velocidad(SUN_MASS, [0, 0, 0])
            planeta_afectado.update_posicion(dt)
            world[f"planet{i}"]["position"] = planeta_afectado.posicion

        world.update()
        cam.update()

        # Here we monitorize the FPS of the simulation
        fps_master_race = 1/dt
        if fps_master_race <=30:
            print(f"FPS: {fps_master_race}")
        #print(1/dt)

    clock.schedule_interval(update, 1 / 165)
    app.run()

"""
=======================================================================================================================


Como ejecutar (o ejecute) la tarea:

Nota de autor:
=======================================================================================================================
"""
