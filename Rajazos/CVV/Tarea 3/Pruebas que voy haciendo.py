# Correspondiente a lo que vaya haciendo en la tarea 3 de CVV   ###########################################
###########################################################################################################
# Parte 2   ###############################################################################################
###########################################################################################################
# Librerias importadas

import numpy as np
import matplotlib.pyplot as plt
###########################################################################################################
# Parte 1, Graficar B(x)

# Grilla eje OX
IntervaloX = np.linspace(-1, 1, 420)

# Funcion B
# Es la solucion planteada de la EDP
def B(x):
    c = (np.pi)/2
    B_x = np.cos(c*x)
    return B_x

# Definimos los valores para el eje OY
IntervaloY = []
exes1 = []
exes2 = []
for i in range(len(IntervaloX)):
    IntervaloY += [B(IntervaloX[i])]
    exes1 += [1]
    exes2 += [-1]

#grafo_Parte_1 = 'si'
grafo_Parte_1 = 'no'
if grafo_Parte_1 == 'si':
    plt.figure(figsize=(7, 5))
    plt.plot(IntervaloX, exes1, "--", color = "0.3")
    plt.plot(IntervaloX, exes2, "--", color = "0.3")
    plt.plot(IntervaloX, IntervaloY, label="$u(x)$", color = "C0")
    plt.title("Grafico de u = B(x) con $x\in [-1, 1]$")
    plt.xlabel("x")
    plt.ylabel("u = B(x)")
    plt.legend()
    plt.show()

###########################################################################################################
# Parte 2, 1) Definir un D = {x}

# Funcion N.
# Toma un numero natural "n" y devuelve una lista de de valores {1,_,j,_,n}.
# Ejemplo: N(10) devolveria una lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
def N(cantidad):
    NN = []
    for i in range(cantidad):
        NN += [i+1]
    return NN


# Funcion xj.
# Toma un natural n, un intervalo de valores y un valor eje 0 o 1 que decide si dara
# valores aleatorios entre el inf(intervalo) y sup(intervalo) o un eje X, es decir
# un vector de n ceros, es decir [0, 0, 0,_, 0] con n cantidad de ceros
def xj(N, intervalo):
    sup = intervalo[1]
    inf = intervalo[0]
    lista_datos_aleatorios = []
    for i in range(N):
        lista_datos_aleatorios += [float(np.random.uniform(inf, sup))]
    return lista_datos_aleatorios


# Parametros usados
n = 100
conjunto = [-1, 1]
xji = xj(n, conjunto)
Nn = N(n)
#print(max(xji), min(xji))


# Bosquejar

#grafo12 = "si"
grafo12 = "no"
if grafo12 == "si":
    plt.figure(figsize=(7, 5))
    plt.plot(Nn, xji, label="Valores aleatorios")
    plt.title("Grafico de "+str(n)+" valores aleatorios \n entre $-1$ y $1$")
    plt.xlabel("Cantidad de valores")
    plt.ylabel("Valores generados")
    plt.legend()
    plt.show()

###########################################################################################################
# Definir parametros extras

# Funcion sigma
# calcula la funcion sigma y su derivada para cualquier orden
def sigma(s, orden):
    assert not orden < 0
    if orden == 0:
        #print('dsen = sen(s) <=> dsen = sen('+str(s)+') = '+str(np.sin(s)))
        return np.sin(s)
    elif orden == 1:
        #print('dsen = cos(s) <=> dsen = cos('+str(s)+') = '+str(np.cos(s)))
        return np.cos(s)
    elif orden == 2:
        #print('dsen = -sen(s) <=> dsen = -sen('+str(s)+') = '+str(-1*np.sin(s)))
        return (-1) * np.sin(s)
    elif orden == 3:
        #print('dsen = -cos(s) <=> dsen = -cos('+str(s)+') = '+str(-1*np.cos(s)))
        return (-1) * np.cos(s)
    else:
        orden = orden - 4
        return sigma(s, orden)


# Funcion Rphi
# Funcion que realiza la red neuronal y sus derivadas ssi orden \in {0, 1, 2}
def R_phi(Phi, x, orden):
    assert not orden < 0
    w1, w2, b1, b2 = Phi
    en_Sigma = w1 * x + b1
    if orden == 0:
        realizacion = w2*sigma(en_Sigma, 0) + b2
        return realizacion
    else:
        if orden == 1:
            cadena_Queda1 = w2*sigma(en_Sigma, 1)
            cadena_Sale1 = w1
            cadena = (cadena_Queda1)*(cadena_Sale1)
            return cadena
        elif orden == 2:
            cadena_Queda2 = w2*sigma(en_Sigma, 2)
            cadena_Sale2 = w1**(2)
            cadena = (cadena_Queda2)*(cadena_Sale2)
            return cadena
        else:
            print('Error en variable D: ')


# Funcion Gradiente_Rphi
# Calcula el gradiente en forma de lista para la funcion Rphi (hasta dos gradientes)
# 1 = 1 realizado gradiente
# 2 = 2 realizado gradientes
def Gradiente_Rphi(Phi, x, nnabla):
    assert not type(nnabla) == str
    w1, w2, b1, b2 = Phi
    en_Sigma = w1 * x + b1
    if nnabla == 1:
        dw1 = w2*sigma(en_Sigma, 1)*w1
        dw2 = sigma(en_Sigma, 0)
        db1 = w2*sigma(en_Sigma, 1)
        db2 = 1
        grad1 = dw1, dw2, db1, db2
        #print('grad(Rphi) = \n', np.array([[dw1], [dw2], [db1], [db2]]))
        #print()
        return grad1
    elif nnabla == 2:
        d2w1 = 2*w1*w2*(sigma(en_Sigma, 2) + sigma(en_Sigma, 3)*x*w2)
        d2w2 = (w2**2)*sigma(en_Sigma, 2)
        d2b1 = w2*w1*sigma(en_Sigma, 3)
        d2b2 = 0
        grad2 = d2w1, d2w2, d2b1, d2b2
        #print("garad(R''phi) = \n", np.array([[d2w1], [d2w2], [d2b1], [d2b2]]))
        #print()
        return grad2
    else:
        print('La cantidad de gradientes que se pueden aplicar son maximo dos ')


def C_phi(u, Phi, D, Condiciones_Borde):
    def Coste_C1(u, Phi, D):
        N = len(D)
        C1=0
        for i in range(N):
            index1 = u(Phi, D[i], orden=2)
            index2 = (((np.pi)**(2))/4) * u(Phi, D[i], orden=0)
            index = ((index1 + index2) ** 2)
            C1 += index
            #print(i+1)
        return C1/N
    def Coste_C2(u, Phi, borde):
        bord1, bord2, bord3 = borde
        parametro_1 = (u(Phi, bord1, orden=0))**2
        parametro_2 = (u(Phi, bord2, orden=0))**2
        parametro_3 = (u(Phi, bord3, orden=0)-1)**2
        C2 = (1/3)*(parametro_1+parametro_2+parametro_3)
        return C2
    Costo1 = Coste_C1(u, Phi, D)
    print('El valor del C1 es: ',Costo1)
    Costo2 = Coste_C2(u, Phi, Condiciones_Borde)
    print('El valor del C2 es: ', Costo2)
    Costo = (1/2)*(Costo1+Costo2)
    print('El valor del C es: ', Costo)
    return Costo


def Gradiente_Cphi(Phi, D):
    N = len(D)
    dc1dw1 = 0
    dc1dw2 = 0
    dc1db1 = 0
    dc1db2 = 0
    pi = ((np.pi) ** 2) / 4
    for i in range(N):
        dw1, dw2, db1, db2 = Gradiente_Rphi(Phi, D[i], 1)
        d2w1, d2w2, d2b1, d2b2 = Gradiente_Rphi(Phi, D[i], 2)
        vive1 = R_phi(Phi, D[i], 2)
        vive2 = (pi*R_phi(Phi, D[i], 0))
        sobrevive = 2*(vive1+vive2)
        purga1 = d2w1 + pi * dw1
        purga2 = d2w2 + pi * dw2
        purga3 = d2b1 + pi * db1
        purga4 = d2b2 + pi * db2
        dc1dw1 += (1/N) * sobrevive * purga1
        dc1dw2 += (1/N) * sobrevive * purga2
        dc1db1 += (1/N) * sobrevive * purga3
        dc1db2 += (1/N) * sobrevive * purga4
        #print(i + 1)
    dc1 = dc1dw1, dc1dw2, dc1db1, dc1db2
    print('El valor del primer componente del gradiente es :', dc1)
    Dc1 = np.array([[dc1dw1], [dc1dw2], [dc1db1], [dc1db2]])
    dw10, dw20, db10, db20 = Gradiente_Rphi(Phi, 0, 1)
    dw11, dw21, db11, db21 = Gradiente_Rphi(Phi, 1, 1)
    dw1n, dw2n, db1n, db2n = Gradiente_Rphi(Phi, -1, 1)
    R0 = R_phi(Phi, 0, 0)
    R1 = R_phi(Phi, 1, 0)
    Rn = R_phi(Phi, -1, 0)
    dc2dw1 = (2/3)*(Rn*(dw1n)+R1*(dw11)+(R0-1)*(dw10))
    dc2dw2 = (2/3)*(Rn*(dw2n)+R1*(dw21)+(R0-1)*(dw20))
    dc2db1 = (2/3)*(Rn*(db1n)+R1*(db11)+(R0-1)*(db10))
    dc2db2 = (2/3)*(Rn*(db2n)+R1*(db21)+(R0-1)*(db20))
    dc2 = dc2dw1, dc2dw2, dc2db1, dc2db2
    print('El valor del segundo componente del gradiente es :', dc2)
    Dc2 = np.array([[dc2dw1], [dc2dw2], [dc2db1], [dc2db2]])
    dcdw1 = (1/2)*(dc1dw1 + dc2dw1)
    dcdw2 = (1/2)*(dc1dw2 + dc2dw2)
    dcdb1 = (1/2)*(dc1db1 + dc2db1)
    dcdb2 = (1/2)*(dc1db2 + dc2db2)
    dc = dcdw1, dcdw2, dcdb1, dcdb2
    print('El vector gradiente esta dado por: \n', (1/2)*(Dc1+Dc2))
    return dc


fifi = 0.5, 1.1, 1.3, 0
fx = np.linspace(-1, 1, 1000)
kond = -1, 1, 0
daboy = C_phi(R_phi, fifi, xji, kond)
ddaboy = Gradiente_Cphi(fifi, fx)
print('El gradiente del costo estaria dado por: grad(C) = ', ddaboy)



###########################################################################################################






