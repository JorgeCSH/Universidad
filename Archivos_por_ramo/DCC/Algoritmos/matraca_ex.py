import numpy as np

def quicksort(a, s):
    # Llama a qsort pasando el límite de elementos a ordenar (s)
    qsort(a, 0, len(a) - 1, s)

def particion(a,i,j): # particiona a[i],...,a[j], retorna posición del pivote
    k=np.random.randint(i,j) # genera un número al azar k en rango i..j
    (a[i],a[k])=(a[k],a[i]) # mueve a[k] al extremo izquierdo
    # a[i] es el pivote
    s=i # invariante: a[i+1..s]<=a[i], a[s+1..t]>a[i]
    for t in range(s,j):
        if a[t+1]<=a[i]:
            (a[s+1],a[t+1])=(a[t+1],a[s+1])
            s=s+1
    # mover pivote al centro
    (a[i],a[s])=(a[s],a[i])
    return s

def qsort(a, i, j, s):
    # Ordena a[i], ..., a[j], considerando solo los primeros s elementos
    if i < j:
        # Llama a la función particion para obtener la posición del pivote
        k = particion(a, i, j)
        # La cantidad de elementos en la izquierda del pivote (incluido el pivote)
        num_left = k - i + 1

        if num_left == s:
            # Si los primeros s elementos están en la izquierda, no se necesita continuar
            return
        elif num_left > s:
            # Si hay más de s elementos en la izquierda, continuar con esa porción
            qsort(a, i, k - 1, s)
        else:
            # Ordenar la izquierda completamente y ajustar s para la derecha
            qsort(a, i, k - 1, num_left - 1)
            qsort(a, k + 1, j, s - num_left)

# Asumiendo que particion está implementada correctamente y retorna el índice del pivote.
# Ejemplo de uso:
#a = [3, 6, 2, 8, 5, 4, 44, 1, 16, 13, 500, 7]
#s = 4
#quicksort(a, s)
#print(a)  # Imprime los s menores elementos ordenados
def findmin(arr):
    """
    Encuentra la posición del mínimo en un arreglo rotado cíclicamente.

    :param arr: List[int] - Un arreglo rotado de números en orden estrictamente ascendente.
    :return: int - Índice del valor mínimo.
    """
    left, right = 0, len(arr) - 1

    # Si el arreglo no está rotado, el primer elemento es el mínimo
    if arr[left] < arr[right]:
        return left

    while left < right:
        mid = (left + right) // 2

        # Verificamos si el elemento en `mid` es mayor que el último
        if arr[mid] > arr[right]:
            # El mínimo está en la parte derecha
            left = mid + 1
        else:
            # El mínimo está en la parte izquierda (incluyendo mid)
            right = mid

    # Al finalizar el bucle, `left` apuntará al índice del mínimo
    return left


# Ejemplo con el arreglo de la imagen
arr = [55, 63, 71, 86, 13, 27, 34, 40, 45, 52]
print(findmin(arr))  # Salida esperada: 3

