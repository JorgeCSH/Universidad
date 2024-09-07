'''
Tarea 2
Jorge Cummins
Version archivo de python
'''

# Importamos librerias
import numpy as np

n = 17
secuencia_invertida = []
di = 1
i = 1
while di < n:
    secuencia_invertida += [di]
    di = int(2 ** i + 1)
    i += 1
secuencia = secuencia_invertida[::-1]
print(secuencia)
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
    n = len(a)
    secuencia_invertida = []
    di = 1
    i = 1
    while di < n:
        secuencia_invertida += [di]
        di = int(2 ** i + 1)
        i += 1
    secuencia = secuencia_invertida[::-1]
    for d in secuencia:
        d_ordena_insercion(a,d)
    return a


# Parte....3 ???/
def Baeza_Yates(n):
    h_0 = n
    H = [h_0]
    for k in range(0, n):
        h_k = max(int(((5*h_0-1)/11)), 1)
        H+=[h_k]
        h_0 = h_k
    return H+[1]


def Shellsort2(a):
    n = len(a)
    secuencia=Baeza_Yates(n)
    for d in secuencia:
        d_ordena_insercion(a,d)
    return a




#######################################################################################################################

# Aca probamos
def verifica_d_ordenado(a,d):
    for i in range(0,len(a)-d):
        assert a[i]<=a[i+d]
    print("Arreglo "+str(d)+"-ordenado OK.")

''' parte 1
A = np.array([46,35,95,21,82,70,72,56,64,50])
d_ordena_insercion(A,3)
print(A)
verifica_d_ordenado(A,3)
'''

''' parte 2
A = np.array([46,35,95,21,82,70,72,56,64,50])
Shellsort(A)
print(A)
verifica_d_ordenado(A,1)


A = np.random.randint(0,1000,1000)
Shellsort(A)
verifica_d_ordenado(A,1)
'''


''' parte 3
Aa = np.array([46,35,95,21,82,70,72,56,64,50])
Shellsort2(Aa)
print(Aa)
verifica_d_ordenado(Aa,1)

# Testeos con valores aleatorios.
# Testeo con 10000
Bb = np.random.randint(0,1000,1000)
Shellsort2(Bb)
verifica_d_ordenado(Bb,1)

# Testeo con 100
Cc = np.random.randint(0, 100, 100)
Shellsort2(Cc)
verifica_d_ordenado(Cc,1)

# Testeo con 10
Dd = np.random.randint(0, 10, 10)
Shellsort2(Dd)
verifica_d_ordenado(Dd, 1)
'''