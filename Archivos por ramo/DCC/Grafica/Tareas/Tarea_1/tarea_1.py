import numpy as np

DEFINITION = 36
def trayectoria(x, y, r, g, b, radius):

    N = DEFINITION
    # Discretizamos un circulo en DEFINITION pasos
    # Cada punto tiene 3 coordenadas y 3 componentes de color
    # Cada triangulo tiene 3 puntos
    # Con N triangulos tenemos 3N puntos
    # El arreglo de posiciones tiene 3 * 3N coordenadas
    # El arreglo de color tiene 3 * 3N componentes
    positions = np.zeros(9*N, dtype=np.float32)
    colors = np.zeros(9*N, dtype=np.float32)
    dtheta = 2*np.pi / N

    for i in range(N):
        x0 = x + np.cos(i*dtheta)*radius
        y0 = y + np.sin(i*dtheta)*radius
        x1 = x + np.cos((i+1)*dtheta)*radius
        y1 = y + np.sin((i+1)*dtheta)*radius

        # centro
        j = i*9
        positions[j:j+3] = [x0, y0, 0.0]
        colors[j:j+3] = [0, 0, 0]
        # p0
        positions[j+3:j+6] = [x0, y0, 0.0]
        colors[j+3:j+6] = [r, g, b]
        # p1
        positions[j+6:j+9] = [x1, y1, 0.0]
        colors[j+6:j+9] = [r, g, b]

    return positions, colors

print(np.ones(4))