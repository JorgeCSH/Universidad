# Librerias importadas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#import pandas as pd
#!git clone                                              #Inserte link de github


########################################################################################################################
################################################# Parte C) #############################################################
########################################################################################################################
# Nombres
# P: P
# Z: Z
# N: N

# Condiciones iniciales
P0 = 0.3
Z0 = 0.1
N0 = 0.6
X0 = P0, Z0, N0

# Constantes
# ctes Edo
M = 0.1
K = 0.2
gamma = 0.3
# ctes g
Vm = 5
k = 1
ctesg = Vm, k
# ctes h
Rm = 3.5
LAMBDA = 0.1
ctesh = Rm, LAMBDA
# Tupla ctes
ctes = M, K, gamma, Vm, k, Rm, LAMBDA

t = (0, 70)

# configuraciones
# Conf1
rtol1 = 10**(-3)                # atol = rtol = configuracion 1
atol1 = 10**(-3)
# Conf2
rtol2 =10**(-13)                # atol = rtol = configuracion 2
atol2 =10**(-13)
########################################################################################################################
########################################################################################################################
# Funciones usadas
# Funcion g(N)
def g(N,Vm,k):
    numerador = Vm*N
    denominador = k + N
    g = numerador/denominador
    return g

# Funcion h(P)
def h(P ,Rm, LAMBDA):
    ashe = Rm*P
    h = ashe + LAMBDA
    return h
########################################################################################################################
########################################################################################################################
# Edo (no lineal)
# Definimos funcion lado derecho
def Fderecho(t, X, ctes):
    P, Z, N = X
    M, K, gamma, Vm, k, Rm, LAMBDA = ctes
    hashe = h(P, Rm, LAMBDA)
    ge = g(N, Vm, k)
    dP = ge*P-hashe*Z - M*P
    dZ = gamma*hashe*Z - K*Z
    dN = (-1)*ge*P + (1-gamma)*hashe*Z + M*P + K*Z
    Qx = np.array([dP, dZ, dN])
    return Qx
########################################################################################################################
########################################################################################################################
# Soluciones
# Ingenieria para los switches xD
#grafico1 = 'yes'               # Grafico 2D NO ERROR
grafico1 = 'no'
#grafico4 = 'yes'               # Grafico 3D NO ERROR
grafico4 = 'no'

grafico2 = 'yes'                # Grafico 2D ERROR CONFIG 1
#grafico2 = 'no'
#grafico5 = 'yes'               # Grafico 3D ERROR CONFIG 1
grafico5 = 'no'

grafico3 = 'yes'                # Grafico 2D ERROR CONFIG 2
#grafico3 = 'no'
#grafico6 = 'yes'               # Grafico 3D ERROR CONFIG 2
grafico6 = 'no'



# Caso sin error (dejar libre al solver)
# Solucion
YhYp = solve_ivp(Fderecho, t, X0, method= "RK45",  args = (ctes,))
I, X = YhYp["t"], YhYp["y"]
P, Z, N = X[0], X[1], X[2]
# Grafico
if grafico1 == 'yes':
    # Figura y tamaño
    plt.figure(figsize=(7,5))
    # Grafico (x, t) ====== x(t)
    plt.plot(I, P, label = "P en torno al tiempo (P(t))")
    plt.plot(I, Z, label = "Z en torno al tiempo (Z(t))")
    plt.plot(I, N, label = "N en torno al tiempo (N(t))")
    # Titulo
    plt.title("Comportamiento de P, Z, N con respecto al tiempo. \n Caso sin error asociado")
    # Ejes
    plt.xlabel("Tiempo")
    plt.ylabel("Variables: P(t), Z(t), N(t)")
    # Leyenda (no mitos)
    plt.legend()
    # Mostrar
    plt.show()
# Grafico 3D (P, Z, N)
if grafico4 == 'yes':
    plt.figure(figsize=(7,5))
    ax = plt.axes(projection='3d')
    ax.plot(P, Z, N)
    ax.set_title(' Grafico para (P, Z, N). \n  Caso sin error asociado ')
    ax.set_xlabel('P')
    ax.set_ylabel('Z')
    ax.set_zlabel('N')
    plt.show()

# Caso con error configuracion 1
# Solucion
YhYp1 = solve_ivp(Fderecho, t, X0, method= "RK45",  args = (ctes,), rtol = rtol1, atol = atol1)
I1, X1 = YhYp1["t"], YhYp1["y"]
P1, Z1, N1 = X1[0], X1[1], X1[2]
# Grafico
if grafico2 == 'yes':
    # Figura y tamaño
    plt.figure(figsize=(7,5))
    # Grafico (x, t) ====== x(t)
    plt.plot(I1, P1, label = "P en torno al tiempo (P(t))")
    plt.plot(I1, Z1, label = "Z en torno al tiempo (Z(t))")
    plt.plot(I1, N1, label = "N en torno al tiempo (N(t))")
    # Titulo
    plt.title("Comportamiento de P, Z, N con respecto al tiempo. \n Caso con error: $10^{-3}$")
    # Ejes
    plt.xlabel("Tiempo")
    plt.ylabel("Variables: P(t), Z(t), N(t)")
    # Leyenda (no mitos)
    plt.legend()
    # Mostrar
    plt.show()
# Grafico 3D (P, Z, N)
if grafico5 == 'yes':
    plt.figure(figsize=(7,5))
    ax = plt.axes(projection='3d')
    ax.plot(P1,Z1,N1)
    ax.set_title(' Grafico para (P, Z, N). \n  Caso con error $10^{-3}$')
    ax.set_xlabel('P')
    ax.set_ylabel('Z')
    ax.set_zlabel('N')
    plt.show()

# Caso con error configuracion 2
# Solucion
YhYp2 = solve_ivp(Fderecho, t, X0, method= "RK45",  args = (ctes,), rtol = rtol2, atol = atol2)
I2, X2 = YhYp2["t"], YhYp2["y"]
P2, Z2, N2 = X2[0], X2[1], X2[2]
# Grafico
if grafico3 == 'yes':
    # Figura y tamaño
    plt.figure(figsize=(7,5))
    # Grafico (x, t) ====== x(t)
    plt.plot(I2, P2, label = "P en torno al tiempo (P(t))")
    plt.plot(I2, Z2, label = "Z en torno al tiempo (Z(t))")
    plt.plot(I2, N2, label = "N en torno al tiempo (N(t))")
    # Titulo
    plt.title("Comportamiento de P, Z, N con respecto al tiempo. \n Caso con error: $10^{-13}$")
    # Ejes
    plt.xlabel("Tiempo")
    plt.ylabel("Variables: P(t), Z(t), N(t)")
    # Leyenda (no mitos)
    plt.legend()
    # Mostrar
    plt.show()
# Grafico 3D (P, Z, N)
if grafico6 == 'yes':
    plt.figure(figsize=(7,5))
    ax = plt.axes(projection='3d')
    ax.plot(P2,Z2,N2)
    ax.set_title(' Grafico para (P, Z, N). \n  Caso con error: $10^{-13}$ ')
    ax.set_xlabel('P')
    ax.set_ylabel('Z')
    ax.set_zlabel('N')
    plt.show()
########################################################################################################################
########################################################################################################################


########################################################################################################################
########################################################################################################################


