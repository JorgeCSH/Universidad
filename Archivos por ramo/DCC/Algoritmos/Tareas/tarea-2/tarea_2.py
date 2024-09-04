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
    """
    Inserta a[k] entre los elementos anteriores a distancia d
    preservando el orden ascendente (versión 2)
    """

    # escriba aquí el código modificado de la función insertar
    # para que haga una d-inserción en lugar de una inserción


# Parte 2: Programar shellsort
def Shellsort(a):
    """Ordena a usando Shell Sort, con la secuencia de valores …,65,33,17,9,5,3,1"""

    # Escriba aquí el código para invocar d_ordena_insercion reiteradamente
    # con la secuencia de valores indicada



# Parte....3 ???/




'''
# Aca probamos
def verifica_d_ordenado(a,d):
    for i in range(0,len(a)-d):
        assert a[i]<=a[i+d]
    print("Arreglo "+str(d)+"-ordenado OK.")

A = np.array([46,35,95,21,82,70,72,56,64,50])
ordena_insercion(A)
print(A)
verifica_d_ordenado(A,1)
'''

