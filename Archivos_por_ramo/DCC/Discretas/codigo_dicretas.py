'''
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
'''

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
        return 4*s1(n-1) + s2(n-1)
    
# Testeos de casos bases (0 y 1) y valores calculados manualmente (2, 3).
assert s1(0) == 0
assert s1(1) == 1
assert s1(2) == 5
assert s1(3) == 23


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
        return s1(n-1) + 2*s2(n-1)

# Testeos casos bases (0 y 1) y valores calculados manualmente (2, 3).
assert s2(0) == 0
assert s2(1) == 1
assert s2(2) == 3
assert s2(3) == 11








