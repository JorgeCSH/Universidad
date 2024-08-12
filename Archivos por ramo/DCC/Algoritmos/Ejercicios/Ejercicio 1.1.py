# Ejercicio 1.1 #######################################################################################################
#######################################################################################################################
"""
# Primera parte #######################################################################################################
# Importamos librerias
import numpy as np

# Funcion minmax
def minmax(a):
    maximo=a[0]                  # Se define el maximo como el primer valor de la lista
    for i in range(1,len(a)):    #--|
        if a[i]>maximo:          #  |--> Se itera comparando el valor maximo, en caso de haber algun valor mayor, el a[i]
            maximo=a[i]          #--|    se reemplaza por ese.
    a.remove(maximo)             # Se remueve el maximo de la lista
    minimo = a[0]                # Se define el maximo como el primer valor de la lista sin el maximo
    for j in range(1,len(a)):    #--|
        if a[j]<minimo:          #  |--> Se itera comparando el valor minimo, en caso de haber algun valor menor, el
            minimo=a[j]          #--|    a[j] se reemplaza por ese.
    a.remove(minimo)             # Se remueve el minimo, no era necesario pero lo agrego por simetria
    return (minimo, maximo)      # Retorna la tupla


# Probar aca
# Listas que se usaran para probar
lista_definida = [10,20,30,40,50]    #--|--> Lista definida, caso especifico.
print(lista_definida)                #--|
lista_indefinida = [np.random.randint(1,100) for i in range(5)] #--|--> Lista indefinida, probar caso genera
print(lista_indefinida)                                                   #--|    o que funciona en cualquier lista
print()

# Probar en las listar
# Lista definida
print(minmax(lista_definida))
# Lista indefinida
print(minmax(lista_indefinida))
'''
Notas de autor: funcion basada en la dada en el ejemplo del apunte de algoritmos y estructuras de datos del capitulo
de ejercicios: "01_Ejercicios.ipynb"
'''
"""
# Segunda parte #######################################################################################################
# Importamos librerias
import numpy as np

lista_par = [np.random.randint(1,100) for i in range(8)]
lista_impar = [np.random.randint(1,100) for j in range(9)]
#print(lista_par)
#print(range(len(lista_impar)//2))
def minmax(a):
    pseudo_largo = len(a)//2
    aux = len(a)%2
    pares = []
    impares = []
    for i in range(pseudo_largo):
        pares +=[a[2*i]]
        impares += [a[2*i +1]]
    pares += impares+a[aux*len(a):aux*len(a)-1]
    print(a)
    print(pares)
    print(impares)




minmax(lista_impar)












#######################################################################################################################
#######################################################################################################################

# Extra ##############################################################################################################

"""
Funcion para encontrar el valor minimo y maximo de una lista

Toma un alista y encuentra el maximo iterando, luego retira el maximo de la lista y vuelve a iterar para encontrar
el minimo en la lista sin el maximo retornando el valor en una tupla.
"""
""" Version con pruebas
def minmax(a):
    maximo=a[0]
    #print(a)                   # --> lista original
    for i in range(1,len(a)):
        if a[i]>maximo:
            maximo=a[i]
    a.remove(maximo)
    #print(a)                   # --> Ver la lista sin el maximo
    minimo = a[0]
    for j in range(1,len(a)):
        if a[j]<minimo:
            minimo=a[j]
    a.remove(minimo)
    #print(a)               #--|
    #print(maximo)          #  |---> Printea los valores, estan para corroborar funcionamiento
    #print(minimo)          #  |
    #print(a)               #--|
    return (minimo, maximo)
print(minmax(b))
"""