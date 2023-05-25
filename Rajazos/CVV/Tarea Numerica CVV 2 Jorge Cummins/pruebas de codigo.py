# Aca hago pruebas con los codigos
import numpy as np


# Funcions o componentes Globales


# phi = np.array([[w1], [w2], [b]])


# Toma dos numeros y devuelve la funcion sigmoid o su derivada
#           -> 0, devuelve la funcion.
#           -> 1, devuelve la derivada en torno a s
def sigmoid(s, tipo):
    e = np.exp(s)
    denominador = (1+e)
    if tipo == 0:
        sigmoide = (e)/(denominador)
        return sigmoide
    elif tipo == 1:
        sigmoide = (e)/((denominador)**2)
        return sigmoide


# Entrega la red neuronal realizada.
# phi contiene los pesos y, el vector bias
# x es el vector input
# tipo es que se quiere calcular.
#           -> 0 = valor sin evaluar "x"
#           -> 1 = valor tras evaluar "sigma(x)"
# Esto es para obtener R(phi), despues hay que hacer C(phi)    D:
# dif es si se quiere el valor derivado o no (algunos, no todos xd)
#           -> 0 = no derivado
#           -> 1 = derivado
# CAMBIOS POR HACER:
#           -> Para evitar definir VARIAS VARIABLES (lo dijo xd), usar
#              multiplicacion de matrices
def realizacion(phi, x, tipo, dif):
    pesos = np.array([[phi[0], phi[1]]])
    b = phi[2]
    valoresTeorico = np.dot(np.transpose(pesos), x)
    valoresNumerico = float(valoresTeorico)
    operando = valoresNumerico + float(b)
    if tipo == 0:
        evalu = operando
        return evalu
    elif tipo == 1:
        evalu = sigmoid(operando, dif)
        return evalu


# Derivadas Parciales
# derivada del tipo dc/dw1

#def parcialw1():
