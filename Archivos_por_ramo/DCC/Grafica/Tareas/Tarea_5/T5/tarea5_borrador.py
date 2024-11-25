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


SUN_MASS = 2
SUN_RADIUS = 1.0
GRAVITY = 2


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

    # Sun light node, we use a point light
    world.add_node("sun_light",
                   light=PointLight(),
                   pipeline=pipeline,
                   position=[0, 0, 0]
                   )

    # Sun node, we attach the sun light to the sun node
    world.add_node(
        "sun",
        attach_to= "sun_light",
        mesh=planet_mesh,
        pipeline=lpipeline,
        scale =  [SUN_RADIUS, SUN_RADIUS, SUN_RADIUS],
        color = [1.0, 0.8, 0.3],
        position = [0, 0, 0],
    )

    # Creation of planets, from 10 to 15
    planets_quantities = np.random.randint(10, 15)
    print(planets_quantities)

    planets_radius_lists = []
    planets_position_lists = []
    planets_mass_lists = []

    for i in range(0, planets_quantities):
        # Planet color
        r = np.random.rand()
        g = np.random.rand()
        b = np.random.rand()
        crayon = [r, g, b]

        # Planet size
        planet_coordx = SUN_RADIUS*((planets_quantities-i)/planets_quantities)/2
        planet_coordy = SUN_RADIUS*((planets_quantities-i)/planets_quantities)/2
        planet_coordz = SUN_RADIUS*((planets_quantities-i)/planets_quantities)/2
        planet_scale = np.array([planet_coordx, planet_coordy, planet_coordz])

        PLANET_RADIUS = (((planet_coordx)**(2))+((planet_coordy)**(2))+((planet_coordz)**(2)))**(1/2)
        planets_radius_lists += [[PLANET_RADIUS, planet_scale]]

        # Planet position
        coin_flipx = np.random.choice([-1, 1], 1)
        coin_flipy = np.random.choice([-1, 1], 1)
        coin_flipz = np.random.choice([-1, 1], 1)

        # Coordinates
        planet_coordx = 0
        planet_coordy = 0
        planet_coordz = 0

        # X coordinate
        if coin_flipx == 1:
            planet_coordx = np.random.randint(SUN_RADIUS+0.2, ( SUN_RADIUS+0.2)*7)
        if coin_flipx == -1:
            planet_coordx = np.random.randint((-SUN_RADIUS-0.2)*7, -SUN_RADIUS-0.2)

        # Y coordinate
        if coin_flipy == 1:
            planet_coordy = np.random.randint(SUN_RADIUS+0.2, ( SUN_RADIUS+0.2)*7)
        if coin_flipx == -1:
            planet_coordy = np.random.randint((-SUN_RADIUS-0.2)*7, -SUN_RADIUS-0.2)

        # Z coordinate
        if coin_flipz == 1:
            planet_coordz = np.random.randint(SUN_RADIUS+0.2, ( SUN_RADIUS+0.2)*7)
        if coin_flipx == -1:
            planet_coordz = np.random.randint((-SUN_RADIUS - 0.2) * 7 , -SUN_RADIUS - 0.2)

        PLANET_POS = np.array([planet_coordx, planet_coordy, planet_coordz]) + planet_scale
        planets_position_lists += [PLANET_POS]

        # Planet generation
        world.add_node(
            name = f"planet{i}",
            mesh = planet_mesh,
            pipeline = pipeline,
            scale = planet_scale,
            material = Material(ambient = crayon,
                                diffuse = [crayon[i]*np.random.rand() for i in range(0, len(crayon))],
                                specular = [crayon[i]*np.random.rand() for i in range(0, len(crayon))]),
        )


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

        # Update planets position, the new position is calculated using the gravity formula and the velocity of the planet
        for i in range(0, planets_quantities):
            world[f"planet{i}"]["position"] = [planets_position_lists[i][0]*np.cos(dt*(i/15)), planets_position_lists[i][1]*np.sin(dt*(i/15)), planets_position_lists[i][2]]

        world.update()
        cam.update()

        fps_master_race = 1/dt
        if fps_master_race < 144:
            if fps_master_race < 60:
                if fps_master_race < 30:
                    print(f"(FPS: {fps_master_race}) Master race community: Seriously, now we are in problems ({fps_master_race})\n")
                print(f"(FPS: {fps_master_race}) Master race community: dirty CONSOLE ENJOYER ({fps_master_race})\n")
            print(f"(FPS: {fps_master_race}) Master race community: UNACCEPTABLE ({fps_master_race})\n")
        print(f"(FPS: {fps_master_race}) Master race community: happy sounds* ({fps_master_race})\n")
        #print(1/dt)

    clock.schedule_interval(update, 1 / 144)
    app.run()

"""
=======================================================================================================================


Como ejecutar (o ejecute) la tarea:

Nota de autor:
=======================================================================================================================
"""