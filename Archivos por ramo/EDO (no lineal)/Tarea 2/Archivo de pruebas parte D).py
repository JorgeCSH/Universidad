# Librerias importadas

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd


########################################################################################################################
########################################################################################################################
#weas mias (jorge)/Universidad/Rajazos/Involucran hackear/EDO (no lineal)/Tarea 2
path = "C:\Users\El pueblo\Desktop\weas mias (jorge)\Universidad\Rajazos\Involucran hackear\EDO (no lineal)\Tarea 2\MA2601TN2023\AtlanticoNorte.csv"
data = pd.read_csv(path)
########################################################################################################################
################################################# Parte D) #############################################################
########################################################################################################################
# Nombres
# P: Fitoplancton
# Z: Zooplancton
# N: Nutrientes

# Condiciones iniciales
P0 = 0.7
Z0 = 0.2
N0 = 0.1
X0 = P0, Z0, N0

# Constantes
ktes = gamma

# Tiempo
lim = 'evaluar'
#lim = 'aplicar limite'
t = (0, 21)                         # Dias

# configuraciones
# Conf2
rtol3 =10**(-13)                   # atol = rtol = configuracion 2
atol3 =10**(-13)
########################################################################################################################
########################################################################################################################


########################################################################################################################
########################################################################################################################
def FatlDerecho(t, X, ktes):
    P, Z, N = X
    gamma = ktes
    dP = (-1)*P*Z
    dZ = gamma*P*Z
    dN = (1-gamma)*P*Z
    Qx = np.array([dP, dZ, dN])
    return Qx


# Alto switch
#ggrafico1 = 'yes'
ggrafico1 = 'no'

# Solucion
FatlIzquierdo = solve_ivp(FatlDerecho, t, X0, method= "RK45",  args = (ktes,), rtol = rtol3, atol = atol3)
I, X = FatlIzquierdo["t"], FatlIzquierdo["y"]
P, Z, N = X[0], X[1], X[2]
# Grafico
if ggrafico1 == 'yes':
    # Figura y tamaño
    plt.figure(figsize=(7,5))
    # Grafico (x, t) ====== x(t)
    plt.plot(I, P, label = "Fitoplancton en funcion del tiempo (P(t))")
    plt.plot(I, Z, label = "Zooplancton en funcion del tiempo (Z(t))")
    plt.plot(I, N, label = "Nutrientes en funcion del tiempo (N(t))")
    # Titulo
    plt.title("Comportamiento de P, Z, N con respecto al tiempo. \n Con rtol = $10^{-13}$ y atol = $10^{-13}$")
    # Ejes
    plt.xlabel("Tiempo (dias)")
    plt.ylabel("Variables: Fitoplancton (P), Zooplancton (Z), Nutrientes (N)")
    # Leyenda (no mitos)
    plt.legend()
    # Mostrar
    plt.show()
# Grafico 3D (P, Z, N)
if ggrafico1 == 'yes':
    plt.figure(figsize=(7,5))
    ax = plt.axes(projection='3d')
    ax.plot(P, Z, N)
    ax.set_title(' Grafico para (P, Z, N). \n  Con rtol = $10^{-13}$ y atol = $10^{-13}$ ')
    ax.set_xlabel('P, Fitoplancton')
    ax.set_ylabel('Z, Zooplancton')
    ax.set_zlabel('N, Nutrientes')
    plt.show()
########################################################################################################################
########################################################################################################################





