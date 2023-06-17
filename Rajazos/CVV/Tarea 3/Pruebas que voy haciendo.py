# Correspondiente a lo que vaya haciendo en la tarea 3 de CVV   ###########################################
###########################################################################################################
# Parte 2   ###############################################################################################
###########################################################################################################
# Librerias importadas

import numpy as np
import matplotlib.pyplot as plt
###########################################################################################################
# Parte 1, Graficar B(x)

# Grilla eje OX
IntervaloX = np.linspace(-1, 1, 420)

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
# Parte 2, 1) Definir un D = {x}

# Funcion N.
# Toma un numero natural "n" y devuelve una lista de de valores {1,_,j,_,n}.
# Ejemplo: N(10) devolveria una lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
def N(cantidad):
    NN = []
    for i in range(cantidad):
        xa = NN+[i+1]
        NN = xa
    return NN


# Funcion xj.
# Toma un natural n, un intervalo de valores y un valor eje 0 o 1 que decide si dara
# valores aleatorios entre el inf(intervalo) y sup(intervalo) o un eje X, es decir
# un vector de n ceros, es decir [0, 0, 0,_, 0] con n cantidad de ceros
def xj(N, intervalo, eje):
    sup = intervalo[1]
    inf = intervalo[0]
    lista_datos_aleatorios = []
    if eje == 0:
        for i in range(N):
            list_de_datos = lista_datos_aleatorios + [0]
            lista_datos_aleatorios = list_de_datos
        return lista_datos_aleatorios
    elif eje == 1:
        for i in range(N):
            lista_de_datos = lista_datos_aleatorios + [float(np.random.uniform(inf, sup))]
            lista_datos_aleatorios = lista_de_datos
        return lista_datos_aleatorios


# Parametros usados
n = 100
conjunto = [-1, 1]
xji = xj(n, conjunto, 1)
ejeX = xj(n, conjunto, 0)
Nn = N(n)
#print(max(xji), min(xji))


# Bosquejar
#grafo11 = "si"
grafo11 = "no"
#grafo12 = "si"
grafo12 = "no"
if grafo11 == "si":
    if grafo12 == "si":
        plt.figure(figsize=(7, 5))
        plt.plot(Nn, xji, label="Valores aleatorios")
        plt.plot(Nn, ejeX, label="Eje 0X de referencia", color = 'black')
        plt.title("Grafico de "+str(n)+" valores aleatorios \n entre $-1$ y $1$")
        plt.xlabel("Cantidad de valores")
        plt.ylabel("Valores generados")
        plt.legend()
        plt.show()
    elif grafo12 == "no":
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
    assert not orden < 0
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
    else:
        orden = orden - 4
        return sigma(s, orden)


# Funcion Rphi
# Funcion que realiza la red neuronal y sus derivadas ssi orden \in {0, 1, 2}
def R_phi(Phi, x, orden):
    assert not orden < 0
    w1, w2, b1, b2 = Phi
    en_Sigma = w1 * x + b1
    if orden == 0:
        realizacion = w2*(en_Sigma) + b2
        return realizacion
    else:
        if orden == 1:
            cadena_Queda1 = w2*sigma(en_Sigma, 1)
            cadena_Sale1 = w1
            cadena = (cadena_Queda1)*(cadena_Sale1)
            return cadena
        elif orden == 2:
            cadena_Queda2 = w2*sigma(en_Sigma, 2)
            cadena_Sale2 = w1**(2)
            cadena = (cadena_Queda2)*(cadena_Sale2)
            return cadena
        else:
            print('Error en variable D: ')


# Funcion Gradiente_Rphi
# Calcula el gradiente en forma de lista para la funcion Rphi (hasta dos gradientes)
# 1 = 1 realizado gradiente
# 2 = 2 realizado gradientes
def Gradiente_Rphi(Phi, x, nnabla):
    assert not type(nnabla) == str
    w1, w2, b1, b2 = Phi
    en_Sigma = w1 * x + b1
    if nnabla == 1:
        dw1 = w2*sigma(en_Sigma, 1)*w1
        dw2 = sigma(en_Sigma, 0)
        db1 = w2*sigma(en_Sigma, 1)
        db2 = 1
        grad1 = [dw1, dw2, db1, db2]
        #print('primer grad(Rphi) = \n', np.array([[dw1], [dw2], [db1], [db2]]))
        #print()
        return grad1
    elif nnabla == 2:
        d2w1 = w2*(sigma(en_Sigma, 1) + sigma(en_Sigma, 2)*(w1**(2)))
        d2w2 = 0
        d2b1 = w2*sigma(en_Sigma, 2)
        d2b2 = 0
        grad2 = [d2w1, d2w2, d2b1, d2b2]
        #print('segundo garad(Rphi) = \n', np.array([[d2w1], [d2w2], [d2b1], [d2b2]]))
        #print()
        return grad2
    else:
        print('La cantidad de gradientes que se pueden aplicar son maximo dos ')


def u(x, orden):
    pass


def Costo(Phi, D, Condiciones_Borde):
    def Coste_C1(u, D):
        N = len(D)
        C1=0
        for i in range(N):
            index1 = u(D[i], orden=2)
            index2 = (((np.pi)**(2))/4) * u(D[i], orden=0)
            index = ((index1 + index2) ** 2)
            C1 += index
            return C1/N
    def Coste_C2(u, borde):
        bord1, bord2, bord3 = borde
        parametro_1 = (u(bord1, orden=0))**2
        parametro_2 = (u(bord2, orden=0))**2
        parametro_3 = (u(bord3, orden=0)-1)**2
        C2 = (1/3)*(parametro_1+parametro_2+parametro_3)
        return C2
    Costo1 = Coste_C1(u, D)
    Costo2 = Coste_C2(u, Condiciones_Borde)
    Costo = (1/2)*(Costo1+Costo2)*(R_phi(Phi, x = D, orden = 0))
    return Costo

###########################################################################################################






