# Librerias importadas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#import pandas as pd
#!git clone                                              #Inserte link de github


########################################################################################################################
################################################# Parte D) #############################################################
########################################################################################################################
# Condiciones iniciales
P0 = 0.7
Z0 = 0.2
N0 = 0.1
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

# Tiempo
lim = 'evaluar'
#lim = 'aplicar limite'
if lim == 'evaluar':                        # No limite aplicado
    t = (0, 70)
elif lim == 'aplicar limite':               # t = 400 ===== t = infinito xD
    t = (0, 400)

# configuraciones
# Conf2
rtol2 =10**(-13)                # atol = rtol = configuracion 2
atol2 =10**(-13)
########################################################################################################################
########################################################################################################################





