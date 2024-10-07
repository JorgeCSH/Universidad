import pyglet
from pyglet.gl import *
from pyglet.graphics.shader import Shader, ShaderProgram
import numpy as np

from grafica.scene_graph import SceneGraph
from grafica.camera import OrbitCamera
from grafica.helpers import mesh_from_files
from grafica.drawables import Model()



# Corresponde al archivo donde voy testeando custiones
''' Funcion create_sphere()
Funcion que, inspirada en la funcion create_ring, crea una
esfera discretizando en coordenadas esfericas phi y theta.

Recibe "definition" que corresponde a la cantidad de divisiones y devuelve Model para crear la esfera.
'''
def create_sphere(definition):
    # Coordenadas de posición (posiciones) para un esfera UV
    positions = np.zeros((definition * definition) * 3, dtype=np.float32) 
    # Coordenadas de texturas (uv)
    uv = np.zeros((definition * definition) * 2, dtype=np.float32)
    # Índices para formar los triángulos
    indices = np.zeros((6 * (definition - 1) * (definition - 1)), dtype=np.int32)

    dtheta = 2 * np.pi / definition  # Resolución azimutal
    dphi = np.pi / definition         # Resolución polar

    # Radios de la esfera
    radius = 1.0

    # Generar posiciones de vértices y coordenadas de texturas (UV)
    for i in range(definition):
        for j in range(definition):
            idx = 3 * (i * definition + j)
            tidx = 2 * (i * definition + j)

            theta = j * dtheta  # Ángulo azimutal
            phi = i * dphi      # Ángulo polar

            # Coordenadas esféricas convertidas a coordenadas cartesianas
            x = radius * np.sin(phi) * np.cos(theta)
            y = radius * np.sin(phi) * np.sin(theta)
            z = radius * np.cos(phi)

            positions[idx:idx+3] = [x, y, z]
            uv[tidx:tidx+2] = [j / (definition - 1), i / (definition - 1)]

    # Generar índices de triángulos
    for i in range(definition - 1):
        for j in range(definition - 1):
            idx = 6 * (i * (definition - 1) + j)
            p0 = i * definition + j
            p1 = p0 + 1
            p2 = p0 + definition
            p3 = p2 + 1

            # Triángulos que forman la malla
            indices[idx:idx+3] = [p0, p1, p2]
            indices[idx+3:idx+6] = [p1, p3, p2]

    return Model(positions, uv, None, indices)

