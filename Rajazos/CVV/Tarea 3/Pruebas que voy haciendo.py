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
# Es la solucion planteada de la EDO
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
    plt.plot(IntervaloX, IntervaloY, label="$u(x)=B(x)=\cos(\\frac{\pi}{2}x)$", color = "green")
    plt.plot(IntervaloX, exes1, "--", label = '$|y|=1$', color = "0.3")
    plt.plot(IntervaloX, exes2, "--", color = "0.3")
    plt.title("Grafico de u = B(x) con $x\in [-1, 1]$")
    plt.xlabel("x")
    plt.ylabel("u = B(x)")
    plt.legend(loc=4)
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
# inf(intervalo) y sup(intervalo) o un eje X, generando N valores
# valore aleatorios entre el inf y el sup
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
    plt.plot(Nn, xji, '*',color = 'black')
    plt.plot(Nn, xji, label="Valores aleatorios", color = 'green')
    plt.title("Grafico de "+str(n)+" valores aleatorios \n entre $-1$ y $1$")
    plt.xlabel("$N$-esimo valor")
    plt.ylabel("Valores generados")
    plt.legend()
    plt.show()

###########################################################################################################
# Definir parametros extras

# Funcion sigma
# calcula la funcion sigma y su derivada para cualquier orden
def sigma(s, orden):
    if orden == 0:
        #print('dsen = sen(s) <=> dsen = sen('+str(s)+') = '+str(np.sin(s)))
        return np.sin(s)
    elif orden == 1:
        #print('dsen = cos(s) <=> dsen = cos('+str(s)+') = '+str(np.cos(s)))
        return np.cos(s)
    elif orden == 2:
        #print('dsen = -sen(s) <=> dsen = -sen('+str(s)+') = '+str(-1*np.sin(s)))
        return (-1) * np.sin(s)
    elif orden == 3:
        #print('dsen = -cos(s) <=> dsen = -cos('+str(s)+') = '+str(-1*np.cos(s)))
        return (-1) * np.cos(s)


# Funcion Rphi
# Funcion que realiza la red neuronal y sus derivadas ssi orden \in {0, 1, 2}
def R_phi(Phi, x, orden):
    w1, w2, b1, b2 = Phi
    if orden == 0:
        realizacion = w2*np.sin(b1+w1*x) + b2
        return realizacion
    elif orden == 1:
        realizacion = w1*w2*np.cos(b1+w1*x)
        return realizacion
    elif orden == 2:
        realizacion= -(w1**2)*w2*np.sin(b1+w1*x)
        return realizacion


# Funcion Gradiente_Rphi
# Calcula el gradiente en forma de lista para la funcion Rphi (hasta dos gradientes)
# 1 = realizado gradiente orden 0
# 2 = realizado gradiente orden 2
def Gradiente_Rphi(Phi, x, nnabla):
    w1, w2, b1, b2 = Phi
    if nnabla == 1:
        dw1 = w2*x*sigma(b1 + w1*x, 1)
        dw2 = sigma(b1 + w1*x, 0)
        db1 = w2*sigma(b1 + w1*x, 1)
        db2 = 1
        grad1 = np.array([dw1, dw2, db1, db2])
        return grad1
    elif nnabla == 2:
        d2w1 = (w1**2)*w2*x*(sigma(b1 + w1*x, 3) + 2*w1*w2*sigma(b1 + w1*x, 2))
        d2w2 = (w1**2)*sigma(b1 + w1*x, 2)
        d2b1 = (w1**2)*w2*sigma(b1 + w1*x, 3)
        d2b2 = 0
        grad2 = np.array([d2w1, d2w2, d2b1, d2b2])
        return grad2



# Funcion C_Phi
# Calcula la funcion de costos de una realizacion
def C_phi(Phi, D):
    w1, w2, b1, b2 = Phi
    N = len(D)
    def Coste_C1(D):
        C1 = 0
        for i in range(N):
            R = w2 * np.sin(b1 + w1 * D[i]) + b2
            R2 = -(w1 ** 2) * w2 * np.sin(b1 + w1 * D[i])
            C1 += (R+R2)**2
            #print(i+1)
        return C1
    U_1 = (w2 * np.sin(-w1 + b1) + b2) ** 2
    U1 = (w2 * np.sin(w1 + b1) + b2) ** 2
    U0 = (1 - w2 * np.sin(b1) + b2) ** 2
    Costo2 = (1/3)*(U_1+U1+U0)
    Costo1 = (1/N)*Coste_C1(D)
    Costo = (1/2)*(Costo1+Costo2)
    return Costo


# Funcion Gradiente_Cphi
# Calcula el gradiente de la funcion de costos
def Grad_C1(Phi, D):
    w1, w2, b1, b2 = Phi
    N = len(D)
    #print(N)
    dC1dw1 = 0
    dC1dw2 = 0
    dC1db1 = 0
    dC1db2 = 0
    for i in range(N):
        dC1dw1 += (1/N)*((-(w1 ** 2) * w2 * np.sin(b1 + w1 * D[i]) + (np.pi ** 2) * (b2 + w2 * np.sin(b1 + w1 * D[i])) / 4) * (-2 * (w1 ** 2) * w2 * D[i] * np.cos(b1 + w1 * D[i]) - 4 * w1 * w2 * np.sin(b1 + w1 * D[i]) + (np.pi ** 2) * w2 * D[i] * np.cos(  b1 + w1 * D[i]) / 2))
        dC1dw2 += (1/N)*((-2 * (w1 ** 2) * np.sin(b1 + w1 * D[i]) + (np.pi ** 2) * np.sin(b1 + w1 * D[i]) / 2) * (-(w1 ** 2) * w2 * np.sin(b1 + w1 * D[i]) + (np.pi ** 2) * (b2 + w2 * np.sin(b1 + w1 * D[i])) / 4))
        dC1db1 += (1/N)*((-(w1 ** 2) * w2 * np.sin(b1 + w1 * D[i]) + (np.pi ** 2) * (b2 + w2 * np.sin(b1 + w1 * D[i])) / 4) * (-2 * (w1 ** 2) * w2 * np.cos(b1 + w1 * D[i]) + (np.pi ** 2) * w2 * np.cos(b1 + w1 * D[i]) / 2))
        dC1db2 += (1/N)*((np.pi ** 2) * (-(w1 ** 2) * w2 * np.sin(b1 + w1 * D[i]) +( np.pi ** 2 )* (b2 + w2 * np.sin(b1 + w1 * D[i])) / 4) / 2)
        #print(i + 1)
    return np.array([dC1dw1, dC1dw2, dC1db1, dC1db2])

def Grad_C2(Phi):
    w1, w2, b1, b2 = Phi
    dC2dw1 = (1/3)*(-2 * w2 * (b2 + w2 * np.sin(b1 - w1)) * np.cos(b1 - w1) + 2 * w2 * (b2 + w2 * np.sin(b1 + w1)) * np.cos(b1 + w1))
    dC2dw2 = (1/3)*(2 * (b2 + w2 * np.sin(b1 - w1)) * np.sin(b1 - w1) + 2 * (b2 + w2 * np.sin(b1 + w1)) * np.sin(b1 + w1) - 2 * (b2 - w2 * np.sin(b1) + 1) * np.sin(b1))
    dC2db1 = (1/3)*(2 * w2 * (b2 + w2 * np.sin(b1 - w1)) * np.cos(b1 - w1) + 2 * w2 * (b2 + w2 * np.sin(b1 + w1)) * np.cos(b1 + w1) - 2 * w2 * (b2 - w2 * np.sin(b1) + 1) * np.cos(b1))
    dC2db2 = (1/3)*(6 * b2 - 2 * w2 * np.sin(b1) + 2 * w2 * np.sin(b1 - w1) + 2 * w2 * np.sin(b1 + w1) + 2)
    return np.array([[dC2dw1, dC2dw2, dC2db1, dC2db2]])

def Gradiente_Cphi(Phi, D):
    gradiente_C1 = Grad_C1(Phi, D)
    gradiente_C2 = Grad_C2(Phi)
    DCC = (1/2)*(gradiente_C1+gradiente_C2)
    dC = np.transpose(DCC)
    return DCC


# Funcion Gradiente_Conjugado
# Calcula la realizacion de el gradiente conjugado para M iteraciones
def Gradiente_Conjugado(M, l, Phi0, D):
    M=M+1
    Phi = np.zeros((M+1, 4))
    Phi[0] = Phi0
    for i in range(M):
        Phi[i + 1] = Phi[i] - l * Gradiente_Cphi(Phi[i], D)
        Phi[i] = Phi[i + 1]
        # print(Phi[i])
        #print(i)
    Phix = float(Phi[-1, 0:4][0]), float(Phi[-1, 0:4][1]), float(Phi[-1, 0:4][2]), float(Phi[-1, 0:4][3])
    return Phix

def G1radiente_Conjugado(M, l, Phi0, D):
    w1, w2, b1, b2 = Phi0
    def gradienteFome(w1, w2, b1, b2, k, l, D, a=0):
        phi = w1, w2, b1, b2
        if k == 0:
            print(a)
            return w1, w2, b1, b2
        else:
            w11 = w1 - (l)*float((Gradiente_Cphi(phi, D)[0]))
            w22 = w2 - (l)*float((Gradiente_Cphi(phi, D)[1]))
            b11 = b1 - (l)*float((Gradiente_Cphi(phi, D)[2]))
            b22 = b2 - (l)*float((Gradiente_Cphi(phi, D)[3]))
            w1 = w11
            w2 = w22
            b1 = b11
            b2 = b22
            return gradienteFome(w1, w2, b1, b2, k - 1, l, D, a=a+1)
    Cgradiente = gradienteFome(w1, w2, b1, b2, M, l, D)
    return Cgradiente


# Valores constantes o parametros constantes
nu = 0.01
M1 = 100
M2 = 500
M3 = 1000
W = 0.5, 1.1, 1.3, 0


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
    Caso_M100 = Gradiente_Conjugado(M1, nu, W, xji)
    print(Caso_M100)

    Caso_M500 = Gradiente_Conjugado(M2, nu, W, xji)
    print(Caso_M500)

    Caso_M1000 = Gradiente_Conjugado(M3, nu, W, xji)
    print(Caso_M1000)

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



#grafc = 'si'
grafc = 'no'
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

