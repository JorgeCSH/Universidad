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

from utils import helpers, scene_graph, drawables, camera


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

    mesh = Sphere(36)

    world.add_node(
        "sun",
        mesh=mesh,
        pipeline=lpipeline,
        scale=np.full(3, SUN_RADIUS),
        color=[1.0, 0.8, 0.3],
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

        world.update()
        cam.update()

    clock.schedule_interval(update, 1 / 60)
    app.run()

"""
=======================================================================================================================


Como ejecutar (o ejecute) la tarea:

Nota de autor:
=======================================================================================================================
"""