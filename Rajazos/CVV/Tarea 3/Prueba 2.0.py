###########################################################################################################
# ANTES: COMO FUNCIONA ESTA CUSTION:

# Los if que estan al comienzo de cada wea son como un switch
# Hay formas mas eficientes pero la verdad tengo que salvar ramos como para darme la paja de aprender

# Funcionamiento: Se le agrega '#' para activar o desactivar
#
# |valor = 'si'          Encendido
# |valor = 'no'          Apagado
# |if valor == 'si':     Matraca


# Forma apagada (no activa ka seccion del codigo):
#
# |#valor = 'si'
# |valor = 'no'
# |if valor == 'si':


# Forma encendida (activa la seccion del codigo):
#
# |valor = 'si'
# |#valor = 'no'
# |if valor == 'si':


# Engineering intensifies
###########################################################################################################
# Correspondiente a lo que vaya haciendo en la tarea 3 de CVV   ###########################################
###########################################################################################################
# Librerias importadas

import numpy as np
import matplotlib.pyplot as plt
from datetime import date

###########################################################################################################
# Parte 1, Graficar B(x) ##################################################################################
###########################################################################################################

# Grilla eje OX
IntervaloX = np.linspace(-1, 1, 500)

# Funcion B
# Es la solucion planteada de la EDP
def B(x):
    c = (np.pi)/2
    B_x = np.cos(c*x)
    return B_x

# Definimos los valores para el eje OY
IntervaloY = []
exes1 = []
exes2 = []
for i in range(len(IntervaloX)):
    IntervaloY += [B(IntervaloX[i])]
    exes1 += [1]
    exes2 += [-1]

#grafo_Parte_1 = 'si'
grafo_Parte_1 = 'no'
if grafo_Parte_1 == 'si':
    plt.figure(figsize=(7, 5))
    plt.plot(IntervaloX, exes1, "--", color = "0.3")
    plt.plot(IntervaloX, exes2, "--", color = "0.3")
    plt.plot(IntervaloX, IntervaloY, label="$u(x)$", color = "C0")
    plt.title("Grafico de u = B(x) con $x\in [-1, 1]$")
    plt.xlabel("x")
    plt.ylabel("u = B(x)")
    plt.legend()
    plt.show()

###########################################################################################################
# Parte 2, Gradiente conjugado y compañia   ###############################################################
###########################################################################################################

# Funcion N.
# Toma un numero natural "n" y devuelve una lista de de valores {1,_,j,_,n}.
# Ejemplo: N(10) devolveria una lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
def N(cantidad):
    NN = []
    for i in range(cantidad):
        NN += [i+1]
    return NN


# Funcion xj.
# Toma un natural n y un intervalo de valores aleatorios entre el
# inf(intervalo) y sup(intervalo) o un eje X, es decir
# un vector de n ceros, es decir [0, 0, 0,_, 0] con n cantidad de ceros
def xj(N, intervalo):
    sup = intervalo[1]
    inf = intervalo[0]
    lista_datos_aleatorios = []
    for i in range(N):
        lista_datos_aleatorios += [float(np.random.uniform(inf, sup))]
    return lista_datos_aleatorios


# Parametros usados
n = 100
conjunto = [-1, 1]
xji = xj(n, conjunto)
Nn = N(n)
#print(max(xji), min(xji))


# Bosquejar
#grafo12 = "si"
grafo12 = "no"
if grafo12 == "si":
    plt.figure(figsize=(7, 5))
    plt.plot(Nn, xji, label="Valores aleatorios")
    plt.title("Grafico de "+str(n)+" valores aleatorios \n entre $-1$ y $1$")
    plt.xlabel("Cantidad de valores")
    plt.ylabel("Valores generados")
    plt.legend()
    plt.show()

###########################################################################################################
# Definir parametros extras


# Funcion sigma
# calcula la funcion sigma y su derivada para cualquier orden
def sigma(s, orden):
    if orden == 0:
        return np.sin(s)
    elif orden == 1:
        return np.cos(s)
    elif orden == 2:
        return -np.sin(s)
    else:
        return -np.cos(s)

# Funcion R_phi
# Funcion que realiza la red neuronal y sus derivadas ssi orden \in {0, 1, 2}
def R_phi(Phi, x, orden):
    w1, w2, b1, b2 = Phi
    en_Sigma = w1 * x + b1
    if orden == 0:
        realizacion = w2 * sigma(en_Sigma, 0) + b2
        return realizacion
    elif orden == 1:
        realizacion = w1 * w2 * sigma(en_Sigma, 1)
        return realizacion
    elif orden == 2:
        realizacion = (w1 ** 2) * w2 * sigma(en_Sigma, 2)
        return realizacion

# Funcion Gradiente_Rphi
# Calcula el gradiente en forma de lista para la funcion Rphi (hasta dos gradientes)
# 1 = realizado gradiente orden 0
# 2 = realizado gradiente orden 2
def Gradiente_Rphi(Phi, x, nnabla):
    w1, w2, b1, b2 = Phi
    en_Sigma = w1 * x + b1
    if nnabla == 1:
        dw1 = w2 * x * sigma(en_Sigma, 1)
        dw2 = sigma(en_Sigma, 0)
        db1 = w2 * sigma(en_Sigma, 1)
        db2 = 1
        grad1 = np.array([dw1, dw2, db1, db2])
        return grad1
    elif nnabla == 2:
        d2w1 = (w1 ** 2) * w2 * x * (sigma(en_Sigma, 2) + sigma(en_Sigma, 3) * 2 * w1 * w2)
        d2w2 = (w1 ** 2) * sigma(en_Sigma, 2)
        d2b1 = (w1 ** 2) * w2 * sigma(en_Sigma, 3)
        d2b2 = 0
        grad2 = np.array([d2w1, d2w2, d2b1, d2b2])
        return grad2

# Funcion C_Phi
# Calcula la funcion de costos de una realizacion
def C_phi(u, Phi, D, Condiciones_Borde):
    def Coste_C1(u, Phi, D):
        N = len(D)
        C1 = 0
        for i in range(N):
            index1 = u(Phi, D[i], orden=2)
            index2 = (((np.pi) ** (2)) / 4) * u(Phi, D[i], orden=0)
            index = ((index1 + index2) ** 2)
            C1 += index
        return C1 / N

    def Coste_C2(u, Phi, borde):
        bord1, bord2, bord3 = borde
        parametro_1 = (u(Phi, bord1, orden=0)) ** 2
        parametro_2 = (u(Phi, bord2, orden=0)) ** 2
        parametro_3 = (u(Phi, bord3, orden=0) - 1) ** 2
        C2 = (1 / 3) * (parametro_1 + parametro_2 + parametro_3)
        return C2

    Costo1 = Coste_C1(u, Phi, D)
    Costo2 = Coste_C2(u, Phi, Condiciones_Borde)
    Costo = (1 / 2) * (Costo1 + Costo2)
    return Costo

# Funcion Gradiente_Cphi
# Calcula el gradiente de la funcion de costos
def Gradiente_Cphi(Phi, D):
    N = len(D)
    Mc1 = np.array([0, 0, 0, 0])
    pi = ((np.pi) ** 2) / 4
    for i in range(N):
        gradR = Gradiente_Rphi(Phi, D[i], 1)
        grad2R = Gradiente_Rphi(Phi, D[i], 2)
        purga = grad2R + pi * gradR
        vive1 = R_phi(Phi, D[i], 2)
        vive2 = (pi * R_phi(Phi, D[i], 0))
        sobrevive = (vive1 + vive2)
        Mc1n = Mc1 + (sobrevive * purga)
        Mc1 = Mc1n

    Jc = np.array([Gradiente_Rphi(Phi, 0, 1), Gradiente_Rphi(Phi, 1, 1), Gradiente_Rphi(Phi, -1, 1)])
    Vc = np.array([(R_phi(Phi, 0, 0) - 1), R_phi(Phi, 1, 0), R_phi(Phi, -1, 0)])
    Mc2 = 2 * 2 * (np.matmul(Vc, Jc))
    dc = ((2 / N) * Mc1 + Mc2)
    return dc

# Funcion Gradiente_Conjugado
# Calcula la realizacion de el gradiente conjugado para M iteraciones
def Gradiente_Conjugado(M, l, Phi0, D):
    M = M + 1
    Phi = np.zeros((M + 1, 4))
    Phi[0] = Phi0
    for i in range(M):
        Phi[i + 1] = Phi[i] - l * Gradiente_Cphi(Phi[i], D)
        Phi[i] = Phi[i + 1]
    return Phi


# Valores constantes o parametros constantes
nu = 0.01
M1 = 100
M2 = 500
M3 = 1000
W = 0.5, 1.1, 1.3, 0
Borde = -1, 1, 0


# Grilla usada para graficar (y otras funciones)
OX = np.linspace(-1, 1, 500)


# Funciones evaluada
#resultado = 'si'
resultado = 'no'
if resultado == 'si':
    Funcion_de_costos = C_phi(R_phi, W, xji, Borde)
    Gradiente_de_costos = Gradiente_Cphi(W, OX)


# Gradientes conjugados (Harta matraca)
Gradientes = 'si'
#Gradientes = 'no'
if Gradientes == 'si':
    Caso_M100 = Gradiente_Conjugado(M1, nu, W, xji)[-1, 0:4]
    W100 = Caso_M100[0], Caso_M100[1], Caso_M100[2], Caso_M100[3]
    print(W100)

    Caso_M500 = Gradiente_Conjugado(M2, nu, W, xji)[-1, 0:4]
    W500 = Caso_M500[0], Caso_M500[1], Caso_M500[2], Caso_M500[3]
    print(W500)

    Caso_M1000 = Gradiente_Conjugado(M3, nu, W, xji)[-1, 0:4]
    W1000 = Caso_M1000[0], Caso_M1000[1], Caso_M1000[2], Caso_M1000[3]
    print(W1000)

    gradM1 = []
    gradM2 = []
    gradM3 = []
    B_x = []
    Cot_sup = []
    Cot_inf = []
    for croissant in range(len(OX)):
        gradM1 += [R_phi(Caso_M100, OX[croissant], 0)]
        gradM2 += [R_phi(Caso_M500, OX[croissant], 0)]
        gradM3 += [R_phi(Caso_M1000, OX[croissant], 0)]
        B_x += [B(OX[croissant])]
        Cot_sup += [1]
        Cot_inf += [-1]

# Bosquejos de las realizaciones
graf = 'si'
#graf = 'no'
if graf == 'si':
    plt.figure(figsize=(7,5))
    plt.plot(OX, gradM1, label = '$\mathcal{R}(\Phi)(x)_{'+str(M1)+'}$', color = 'purple')
    plt.plot(OX, gradM2, label = '$\mathcal{R}(\Phi)(x)_{'+str(M2)+'}$', color = 'blue')
    plt.plot(OX, gradM3, label = '$\mathcal{R}(\Phi)(x)_{'+str(M3)+'}$', color = 'green')
    plt.plot(OX, B_x, label = '$B(x) = \cos(\\frac{\pi}{2} x)$', color = 'red')
    plt.plot(OX, Cot_sup, "--", color="0.3")
    plt.plot(OX, Cot_inf, "--", color="0.3")
    plt.title("Realizaciones \n $\mathcal{R}(\Phi)(x)$ y $B(x) = \cos(\\frac{\pi}{2} x)$")
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.legend()
    plt.show()

Cgrilla = np.linspace(100, 1000, 10)
C_1y1 = []
for i in range(len(Cgrilla)):
    grad = Gradiente_Conjugado(int(Cgrilla[i]), nu, W, xji)[-1, 0:4]
    C_1y1 += [(grad[0], grad[1], grad[2], grad[3])]

C_y = []
for j in range(len(C_1y1)):
    C_y += [C_phi(R_phi, C_1y1[j], xji, Borde)]

grafc = 'si'
#grafc = 'no'
if grafc == 'si':
    plt.figure(figsize=(7,5))
    plt.scatter(Cgrilla, C_y, label='Costos', color='grey')
    plt.plot(Cgrilla, C_y, label = 'Funcion de Costos', color = 'green')
    plt.title("Funcion de Costos $C$ para 10 M-iteraciones entre 100 y 1000")
    plt.xlabel("$M$")
    plt.ylabel("$C(W^{M})$")
    plt.legend()
    plt.show()



###########################################################################################################
# Creditos  ###############################################################################################
###########################################################################################################
#ssss = 'si'
ssss = 'no'
if ssss == 'si':
    fecha_actual = date.today()
    fecha_forma_normal = fecha_actual.strftime("%d/%m/%Y")

    print()
    print('Emition date: ', fecha_forma_normal)
    print()
    print('Developer: <autismus_prime>')
    print()
    print('Copyright Jorgitosoft, all rights reserved')
    print('Designed by Jorgitosoft at 335 East Sand Hill Road Silicon Valley, California')

