import pyglet
import numpy as np
from pyglet.gl import *

WIDTH = 1000
HEIGHT = 1000
DEFINITION = 36

window = pyglet.window.Window(WIDTH, HEIGHT, "Tarea 1 - Sistema Solar")

# Funcion encargada de crear la trayectoria de un planeta
# La funcion retorna la trayectoria en un arreglo de posiciones de un circulo en posicion x,y
# y radio "radius"
def crear_trayectoria(x, y, radius):
    N = DEFINITION
    positions = np.zeros(3*N, dtype=np.float32)
    colors = np.zeros(9 * N, dtype=np.float32)
    dtheta = 2*np.pi / N

    for i in range(N):
        x0 = x + np.cos(i*dtheta)*radius
        y0 = y + np.sin(i*dtheta)*radius

        j = i*3
        positions[j:j+3] = [x0, y0, 0.0]

    return positions

