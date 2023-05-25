# Aca hago pruebas con los codigos
import numpy as np


# Funcions o componentes Globales

# phi = np.array([[w1], [w2], [b]])
# print(len([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))



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



# Funcion que transforma los datos en los calculados en parte practica
# Recibe phi, datos, el N cantidad de datos y los tipos1 y 2
#           si tipo1 = 0, realiza operacion normal
#           si tipo1 = 1, realiza diferencial
#                           si tipo2 = 0, hace w1
#                           si tipo2 = 1, hace w2
#                           si tipo2 = 2, hace b
def transformador(phi, datos, tipo1, tipo2, N):
    if tipo1 == 0:
        for i in range(N):
            pdato = [] + [(realizacion(phi, np.transpose(np.array(datos[i][0:2])), tipo=1, dif=0) - datos[i][2:3]) ** 2]
            ndato = pdato
            return ndato
    elif tipo1 == 1:
        if tipo2 == 0:
            for i in range(N):
                pdato = [] + [(realizacion(phi, np.transpose(np.array(datos[i][0:2])), tipo=1, dif=1) - datos[i][2:3])*datos[i][0]]
                ndato = pdato
                return ndato
        elif tipo2 == 1:
            for i in range(N):
                pdato = [] + [(realizacion(phi, np.transpose(np.array(datos[i][0:2])), tipo=1, dif=1) - datos[i][2:3])*datos[i][1]]
                ndato = pdato
                return ndato
        elif tipo2 == 2:
            for i in range(N):
                pdato = [] + [(realizacion(phi, np.transpose(np.array(datos[i][0:2])), tipo=1, dif=1) - datos[i][2:3])]
                ndato = pdato
                return ndato



# Funcion que va evaluando el costo en una matriz con inputs y outputs
# Recibe phi, datos y los tipos de operaciones
#          si tipo1 = 0, calcula el coste de esta
#          si tipo1 = 1, comienza a derivar
#                   si tipo2 = 0, deriva en w1
#                   si tipo2 = 1, deriva en w2
#                   si tipo2 = 2, deriva en b
def costo(phi, tipo1, tipo2, datos):
    N = len(datos)
    original = transformador(phi, datos, tipo1, tipo2, N)
    dC = np.transpose(np.array(original))
    if tipo1 == 0:
        sumCosto = sum(original)
        costoRealizacion = sumCosto/2
        return costoRealizacion
    elif tipo1 == 1:
        if tipo2 == 0:
            dw1 = transformador(phi, datos, 1, 0, N)
            dw11 = np.array(dw1)
            costoRealizacion = np.dot(dC, dw11)
            return costoRealizacion
        elif tipo2 == 1:
            dw2 = transformador(phi, datos, 1, 1, N)
            dw22 = np.array(dw2)
            costoRealizacion = np.dot(dC, dw22)
            return costoRealizacion
        elif tipo2 == 2:
            db = transformador(phi, datos, 1, 2, N)
            dbb = np.array(db)
            costoRealizacion = np.dot(dC, dbb)
            return costoRealizacion



def gradienteConjugado(m, w1, w2, b):
    M = m+1
    l = 0.01
    def W(M, w1, i=0):
        w = w1







# Derivadas Parciales
# derivada del tipo dc/dw1

#def parcialw1():
