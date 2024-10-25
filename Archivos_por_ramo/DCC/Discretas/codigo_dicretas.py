"""
======================================================================
Trabajo Grupal Matematicas Discretas para la Computacion (CC3101) 
----------------------------------------------------------------------
Integrantes: 
    -> Alonso Alarcon.
    -> Pablo Reyes Pomes
    -> Arturo Arias.
    -> Jorge Cummins Holger.

Cuerpo Docente:
    -> Profesor de Catedra: Federico Olmedo.
    -> Profesor(es) Auxiliar(es): Carlos Antil y Hector Jimenez.
----------------------------------------------------------------------
Palabras Previas:
    Este codigo contiene el desarrollo de los codigos utilizados en la
    del curso "Matematicas Discretas para la Computacion". El codigo
    fue seccionado en dos donde la parte 1 contiene el codigo asociado
    a la pregunta 1, mientras que la parte 2 asociado a la 
    implementacion mediante exponienciacion de la pregunta 3.

    Este trabajo fue realizado en conjunto entre todos los integrantes
    del equipo.
=======================================================================
"""

# Seccion 1: importamos las librerias utilizadas #####################
######################################################################
import numpy as np


# Seccion 2: Desarrollo ###############################################
#######################################################################

'''
Parte 1: en esta parte desarrollamos un codigo asociado a la pregunta 1
del desarrollo de la tarea grupal. En este caso correspondio a dos
funciones recursivas dependientes entre si las cuales devuelvan las
formas diferentes de subdividir un rectangulo donde el ultimo rectangulo
sea de ancho 1 o 2.

De esta forma, sean:
    s1(n): funcion recursiva para rectangulo de ancho 1.
    s2(n): funcion recursiva para rectangulo de ancho 2.
'''

''' Funcion s1(n)
Funcion que realiza la recurrencia cuando el ultimo rectangulo es de ancho 1.
'''
def s1(n):
    # Caso base donde la altura es 0, es cero pues no hay rectangulo.
    if n == 0:
        return 0
    # Caso base donde la altura es 1.
    if n == 1:
        return 1
    # Caso recursivo. 
    else:
        assert n>=2
        return 4*s1(n-1) + s2(n-1)
    

''' Funcion s2(n)
Funcion que realiza la recurrencia cuando el ultimo rectangulo es de ancho 2.
'''
def s2(n):
    # Caso base donde altura es 0, analogo al de s1(0).
    if n == 0:
        return 0
    # Caso base donde la altura es 1.
    if n == 1:
        return 1
    # Caso recursivo.
    else:
        assert n>=2
        return s1(n-1) + 2*s2(n-1)


''' Funcion s(n)
Funcion que realiza el calculo de las formas diferentes solicitadas, esto 
considerando s1(n) y s2(n).
'''
def s(n):
    assert type(n) == int
    # Caso donde el ancho es 0, analogo a s1 y s2.
    if n == 0:
        return 0
    # Casos donde n>=2, este no es recursivo, s1 y s2 si lo son.
    else:
        assert n>=1
        return s1(n)+s2(n)


# Testeos de casos bases (0 y 1) y valores calculados manualmente (2, 3).
assert s1(0) == 0
assert s1(1) == 1
assert s1(2) == 5
assert s1(3) == 23

# Testeos casos bases (0 y 1) y valores calculados manualmente (2, 3).
assert s2(0) == 0
assert s2(1) == 1
assert s2(2) == 3
assert s2(3) == 11

# Testeos para valores calculados manualmentes (2, 3).
assert s(2) == 8
assert s(3) == 34


# Aca printeamos los valores obtenidos para un n-esimo
#n_esimo = int(input("Inserte largo n "))
n_esimo = 5
for i in range(0, n_esimo):
    print(f"s1({i}) = {s1(i)}")
    print(f"s2({i}) = {s2(i)}")
    print(f"s({i}) = {s(i)}")
    print()


'''
Parte 2: en esta parte veremos una implementacion mas eficiente, donde definiremos una matriz para 
resolver las recurrencias usando el metodo de exponenciacion.
'''


def exponencial(A, n):
    # Se considera hasta el n-1 para el calculo normal
    n = n-1
    # Definimos el ve
    A_mat = np.eye(2, dtype=int)
    i = n
    A_aux = A
    while i > 0:
        while i % 2 == 0:
            A_aux = np.dot(A_aux, A_aux)
            i //= 2
        A_mat = np.dot(A_mat, A_aux)
        i-=1

    return A_mat 


def s_exponenciacion(n):
    
    # Caso de alto 0, analogo al S1 y S2 que originalmente se consideraba
    if n == 0:
        return 0 
    
    # Matriz A correspondiente a la encontrada en la pregunta 3 con respecto a [[s2(n)], [s1(n)]]
    A = np.array([[2, 1], [1, 4]], dtype=int)
    
    # Aca obtenemos la matriz n-esima  
    A_n_esima = exponencial(A, n)
    
    # Vector para casos bases de n=1 ([s2(1), s2(1)]), por eso np.ones
    s_n_1 = np.ones((2, 1))
    
    # Multiplicacion matricial entre la matriz exponenciada y el arreglo s1(n-1) y s2(n-1)
    sn = np.dot(A_n_esima, s_n_1)
    
    # Obtenemos el valor del arreglo
    s_aux = int((sn[0] + sn[1])[0])
    
    # Testeo para corroborar que el valor da lo que deberia dar segun la recurrencia original
    assert s(n) == s_aux
    
    return s_aux


n_exponenciacion = 5
for i in range(0, n_exponenciacion):
    print(f"S({i}) = {s_exponenciacion(i)}")

