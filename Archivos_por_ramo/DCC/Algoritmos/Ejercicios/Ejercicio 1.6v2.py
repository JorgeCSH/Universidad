# Desarrollo ejercicio 1.6

# Importamos las librerias que seran usadas
import numpy as np


'''
Función permutaciones, toma un arreglo de numpy x iniciando en un valor "ini" y terminando en un valor fin 
(ambos fijos).
La función, si bien está implementada con arreglos de numpy, también funciona con listas de Python.
La función toma el arreglo y si la posición inicial es igual a la final, se imprime esa variable de la permutación. Si 
no corresponde a la variable final, se realiza un ciclo iterativo "for" donde se vuelve a llamar a la función 
de manera recursiva aumentando en 1 el valor del índice final, además de invertir los valores en la posición "i" con
el de la posición "ini" para crear una nueva variable de la permutación.
El caso general toma un arreglo x, un valor inicial "ini = 0" y final "fin = len(x) - 1", pues asi recorre todos los 
valores del arreglo.

Esta funcion toma un arreglo x, lo transforma en un arreglo x[ini: fin+1] y lo permuta.
'''
def permutaciones(x, ini, fin):
    if ini == fin:
        print(x)
    else:
        for i in range(ini, fin+1):
            x[i], x[ini] = x[ini], x[i]
            permutaciones(x, ini + 1, fin)
            x[i], x[ini] = x[ini], x[i]





'''
Ejemplo de uso. 

Este originalmente fue probado con arreglo para valores aleatorios, debería ser el mismo resultado pero
con los números aleatorios. 
Se decidió dejar el caso más simple para que sea más fácil de visualizar (por lo menos para mi mientras desarrollo
el ejercicio).

Nota de autor: en el x1 se cambió el 1 para evitar monotonía (y dejar una referencia escondida).
'''
x1 = np.array([42])                         # Arreglo de 1 elemento, debe retornar una permutacion
x2 = np.array([1, 2, 3])                    # Arreglo de 3 elementos, debe retornar 6 permutaciones
x3 = np.array([1, 2, 3, 4, 5])              # Arreglo de 5 elementos, debe retornar 120 permutaciones

#print(x1)                                   # -|    |Imprime las listas usadas. Aca no tiene mucha utilidad, sin embargo
#print(x2)                                   #  |--> |es util si usamos valores aleatorios y ver como, como por ejemplo:
#print(x3)                                   # -|    |x3 = np.random.randint(1, 10, 5)
#permutaciones(x1, 0, len(x1)-1)               # -|
permutaciones(x2, 0,len(x2)-1)               #  |---> Llamamos a la función con los arreglos de ejemplo
#permutaciones(x3, 0, len(x3)-1)               # -|


"""for i in range(len(x2)):
    permutaciones(x2, 0, i)"""

