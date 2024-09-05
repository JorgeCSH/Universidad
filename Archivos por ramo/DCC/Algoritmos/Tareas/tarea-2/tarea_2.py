'''
Tarea 2
Jorge Cummins
Version archivo de python
'''

# Importamos librerias
import numpy as np


# Codigo

# Parte 1: Programar d-ordenacion
def d_ordena_insercion(a,d):
    """d-Ordena el arreglo a por inserción"""
    n=len(a)
    for k in range(0,n):
        d_insertar(a,k,d)


def d_insertar(a,k,d):
    b=a[k]
    j=k-d
    while j>=0 and a[j]>b:
        a[j+d]=a[j]
        j-=d
    a[j+d]=b



# Parte 2: Programar shellsort
def Shellsort(a):
    """Ordena a usando Shell Sort, con la secuencia de valores …,65,33,17,9,5,3,1"""
    # Escriba aquí el código para invocar d_ordena_insercion reiteradamente
    # con la secuencia de valores indicada
    n = 6
    secuencia_sin_uno = []
    for i in range(n, 0, -1):
        secuencia_sin_uno += [2 ** i + 1]
    secuencia = secuencia_sin_uno + [1]
    for d in secuencia:
        d_ordena_insercion(a,d)
    return a



# Parte....3 ???/





# Aca probamos
def verifica_d_ordenado(a,d):
    for i in range(0,len(a)-d):
        assert a[i]<=a[i+d]
    print("Arreglo "+str(d)+"-ordenado OK.")

'''
A = np.array([46,35,95,21,82,70,72,56,64,50])
d_ordena_insercion(A,3)
print(A)
verifica_d_ordenado(A,3)
'''

A = np.array([46,35,95,21,82,70,72,56,64,50])
Shellsort(A)
print(A)
verifica_d_ordenado(A,1)
'''
En la siguiente celda agregue una prueba similar de ordenación de un arreglo de tamaño $1000$ generado al azar (sin imprimirlo):

'''
A = np.random.randint(0,1000,1000)
Shellsort(A)
verifica_d_ordenado(A,1)


