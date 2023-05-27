# Aca hago pruebas con los codigos
import numpy as np



# Funcions o componentes Globales




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
    pesos = np.array([[float(phi[0]), float(phi[1])]])
    b = phi[2]
    valoresTeorico = np.dot(pesos, np.transpose(x))
    valoresNumerico = float(valoresTeorico)
    operando = valoresNumerico + float(b)
    if tipo == 0:
        evalu = sigmoid(operando, dif)
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



# Funcion que calcula el gradiente conjugado de la red neuronal
# Itera con el fin de encontrar un Phi que se parezca al de realizar una red neuronal iterada
# recibe k, o cantidad de iteraciones
# w1, w2, b, valores de un phi aleatorio
# Recibe datos de la realizacion
def gradienteConjugado(k, w1, w2, b, l, datos):
    M = k+1
    w01 = w1
    w02 = w2
    b0 = b
    phix = np.array([[w01], [w02], [b0]])
    if M == 0:
        return phix
    else:
        nw1 = float(phix[0])-(l)*(costo(phix, 1, 0, datos))
        nw2 = float(phix[1])-(l)*(costo(phix, 1, 0, datos))
        nb0 = float(phix[2])-(l)*(costo(phix, 1, 0, datos))
        w1 = float(nw1)
        w2 = float(nw2)
        b = float(nb0)
        return gradienteConjugado(k-1, w1, w2, b, l, datos)



# Desarrollo final
#   I. Ejecutar el gradiente para obtener el (wk1, wk2, bk2)
#   II. Llamando "phi = gradiente conjugado", ejercutamos la
#       realizacion en (8, 7) y phi
#   III. Lloramos porque tendre algun error que no encontrare
#
# Datos:
#    1) croissant: Phi arbitrario que se usara, se definio usando Numpy
#    2) D: vector de datos que se usaran. Fue definido como
#                           -> lista => d
#                           -> matricialmente => D
#    3) X0: vector a evaluar por la realizacion. Fue escrito como:
#                           -> lista => x0
#                           -> vector => X0
#    4) k: numro del "M" de iteraciones. Si bien k = {1,_,M} => |k| = M+1, este "+1" se agrego en la funcion final
#    5) l: learning rate de la red neuronal
croissant = np.random.uniform(size=(3, 1), low=0, high=1)
w1 = float(croissant[0])
w2 = float(croissant[1])
b = float(croissant[2])
d = [[9.0, 7.0, 0.0], [2.0, 5.0, 1.0], [3.2, 4.94, 1.0], [9.1, 7.46, 0.0], [1.6, 4.83, 1.0], [8.4, 7.46, 0.0], [8.0, 7.28, 0.0], [3.1, 4.58, 1.0], [6.3, 9.14, 0.0], [3.4, 5.36, 1.0]]
D = np.array(d)
x0 = [[8, 7]]
X0 = np.array(x0)
k = 1000
l = 0.01



# I.
phiconjugado = gradienteConjugado(1000, w1, w2, b, l, D)
print(phiconjugado)
#print(np.array([[w1], [w2], [b]]))
# II.
redrealizada = realizacion(phiconjugado, X0, 0, 0)
print(redrealizada)


