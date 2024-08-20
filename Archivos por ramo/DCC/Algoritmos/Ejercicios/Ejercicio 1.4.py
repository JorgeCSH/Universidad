# Ahora si ejercicios 1.4 xD

import numpy as np

A = np.array([[10,17,25,36,50,82],
           [15,19,28,45,63,87],
           [21,30,42,56,77,91],
           [27,35,74,84,90,95],
           [40,62,81,86,93,98]])
print(A)


# Funcion
# Busca x en la matriz A
def busca(x,A):
  (m,n)=np.shape(A)
  i = 0
  j = n-1
  while not (i,j) == (m-1,0):
    if A[i,j]==x:
      return (i,j)
    elif A[i,j]>x:
      j-=1
    elif A[i,j]<x:
      i+=1




print(busca(28, A))  # Debe imprimir (1,2)

print(busca(82,A)) # Debe imprimir (0,5)

print(busca(33,A)) # Debe imprimir None

