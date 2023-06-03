# Correspondiente a lo que vaya haciendo en la tarea 3 de CVV   ###########################################
###########################################################################################################
# Parte 2   ###############################################################################################
###########################################################################################################
# Librerias importadas

import numpy as np
import matplotlib.pyplot as plt

###########################################################################################################
# Parte 2,1) Definir un D = {x}

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
n = 1
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
        print('dsen = sen(s) <=> dsen = sen('+str(s)+') = '+str(np.sin(s)))
        return np.sin(s)
    elif orden == 1:
        print('dsen = cos(s) <=> dsen = cos('+str(s)+') = '+str(np.cos(s)))
        return np.cos(s)
    elif orden == 2:
        print('dsen = -sen(s) <=> dsen = -sen('+str(s)+') = '+str(-1*np.sin(s)))
        return (-1) * np.sin(s)
    elif orden == 3:
        print('dsen = -cos(s) <=> dsen = -cos('+str(s)+') = '+str(-1*np.cos(s)))
        return (-1) * np.cos(s)
    else:
        orden = orden - 4
        return sigma(s, orden)


###########################################################################################################







