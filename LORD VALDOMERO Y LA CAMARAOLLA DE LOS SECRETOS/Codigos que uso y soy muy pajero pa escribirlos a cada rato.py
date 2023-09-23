# Principalmete codigos asociados a graficar

import matplotlib.pyplot as plt
import numpy as np


# Funciones de ejemplo
def g(x):
    gi = np.exp(-(x**2))
    return gi

def f(x,y):
    fij = np.exp(-(x**2)-(y**2))
    return fij


# Valores graficar
# 2D
xx = np.linspace(-2, 2, 420)
fredogodofredo = []
for k in range(len(xx)):
    fredogodofredo += [g(xx[k])]

# 3D
x = np.linspace(-2, 2, 420)
y = np.linspace(-2, 2, 420)
z = np.zeros((420, 420))
X,Y = np.meshgrid(x,y)
k=0
planoL = []
while k < len(X):
      planoL += [k]
      k = k + 1
planoR = planoL
for i in planoR :
    for j in planoR:
        z[i,j]=f(X[i,j], Y[i,j])



# Grafico en 2d
plt.figure(figsize=(7,5))
plt.plot(xx, fredogodofredo, label = 'Nombre curva')
plt.title("Titulo del grafico")
plt.xlabel("Titulo eje x")
plt.ylabel("Titulo eje y")
plt.legend()
plt.show()

# Grafico en 3d
plt.figure(figsize=(7,5))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, z)
ax.set_title('Titulo del grafico')
ax.set_xlabel('Titulo eje X')
ax.set_ylabel('Titulo eje Y')
ax.set_zlabel('Titulo eje Z')
plt.show()