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
    # coordenadas de posición
    positions = np.zeros((definition)*3*3 , dtype=np.float32) 
    # coordenadas de texturas
    uv = np.zeros((definition)*3*3, dtype=np.float32)
    dtheta = 2*np.pi / definition
    dphi = np.pi / definition
    r = 1.0

    for i in range(definition):
        idx = 3*i
        tidx = 2*i
        phi = (i+1)*dphi
        theta = i*dtheta
        positions[idx:idx+3] = [np.cos(theta)*np.sin(phi)*r, np.sin(theta)*np.sin(phi)*r, np.cos(phi)*r] 
        uv[tidx:tidx+2] = [theta/(2*np.pi), phi/np.pi]
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
   
    # Completamos la esfera
    idx = 6*(definition-1)
    # t0
    indices[idx:idx+3] = [definition-1, 0, definition-1+definition]
    # t1
    indices[idx+3:idx+6] = [0, definition, definition-1+definition]
    return Model(positions, uv, None, indices)




