'''
Ejercicio 3.5 version archivo de python
Enunciado:

Modifique la funcion para que marque con "." los casilleros por donde hubo intentos no exitosos de salir, y con "x"
los casilleros que finalmente condujeron a la salida.
'''
def salida_original(i,j):
    if L[i][j]=="=": # encontramos la salida
        return True
    if L[i][j]!=" ": # espacio ocupado
        return False
    L[i]=L[i][:j]+"x"+L[i][j+1:]
    if salida(i,j-1) \
    or salida(i,j+1) \
    or salida(i-1,j) \
    or salida(i+1,j):
        return True
    return False


# Modificacion
def salida(i, j):
    if L[i][j]=="=": # encontramos la salida
        return True
    if L[i][j]!=" ": # espacio ocupado
        return False
    L[i]=L[i][:j]+"x"+L[i][j+1:]
    if (salida(i, j-1)
    or salida(i, j+1)
    or salida(i-1, j)
    or salida(i+1, j)):
        return True
    # Si no es exitoso, marcamos con "."
    L[i] = L[i][:j] + "." + L[i][j+1:]
    return False


L = [
"+--+-----+--+",
"|  |     |  |",
"|  +--+     =",
"|     |  |  |",
"+--+  |  |  |",
"|  |        |",
"|  |     |  |",
"+--+-----+--+"
]
print(salida(4,10))
for linea in L:
    print(linea)


'''
Ademas, pruebe el caso salida (1,1) y muestre el resultado.
'''
L = [
"+--+-----+--+",
"|  |     |  |",
"|  +--+     =",
"|     |  |  |",
"+--+  |  |  |",
"|  |        |",
"|  |     |  |",
"+--+-----+--+"
]
print(salida(1,1))


for linea in L:
    print(linea)