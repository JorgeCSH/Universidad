# Funciones que cree haciendo la tarea y no queria perder xD

def nice(i=1):
    numero = int(input('Inserte Numero '))
    while not numero == 69:
        return nice(i=i+1)
    else:
        if i == 1:
            print('Te demoraste 1 intentos en darte cuenta de esto, ¡Felicitaciones!... nice')
        else:
            print('Te demoraste ' + str(i) + ' intentos en darte cuenta de esto, nice')


opa = nice()

# Funcion para mostrar resultado
def matraca(starter1, starter2, juego):
    I, X = starter1
    P, Z, N = starter2
    YhYp = juego
    print('Opciones: ')
    print('1 == I, 2 == P, 3 == Z, 4 == N, 5 == YhYp')
    deseado = input('Cual solucion desea? ')
    if deseado == '1':
        print('I: ')
        print(I)
        matraca(starter1, starter2, juego)
    elif deseado == '2':
        print('P: ')
        print(P)
        matraca(starter1, starter2, juego)
    elif deseado == '3':
        print('Z: ')
        print(Z)
        matraca(starter1, starter2, juego)
    elif deseado == '4':
        print('N: ')
        print(N)
        matraca(starter1, starter2, juego)
    elif deseado == '5':
        print('YhYp')
        print(YhYp)
        matraca(starter1, starter2, juego)
    else:
        print('Gil ')
#matraca(, , )                                      # Muestra Resultado
