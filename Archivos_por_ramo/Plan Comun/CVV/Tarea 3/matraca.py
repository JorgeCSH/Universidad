# Este literal es un codigo para hacer matraca  ############################################################
############################################################################################################
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.abc import a,s,t, N, j

############################################################################################################
# Grilla eje OX
IntervaloX = np.linspace(-1, 1, 500)

# Funcion B
# Es la solucion planteada de la EDO
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
    plt.plot(IntervaloX, IntervaloY, label="$u(x)=B(x)=\cos(\\frac{\pi}{2}x)$", color = "green")
    plt.plot(IntervaloX, exes1, "--", label = '$|y|=1$', color = "0.3")
    plt.plot(IntervaloX, exes2, "--", color = "0.3")
    plt.title("Grafico de u = B(x) con $x\in [-1, 1]$")
    plt.xlabel("x")
    plt.ylabel("u = B(x)")
    plt.legend(loc=4)
    plt.show()

###########################################################################################################
# Parte 2, Gradiente conjugado y compañia   ###############################################################
###########################################################################################################

# Funcion N.
# Toma un numero natural "n" y devuelve una lista de de valores {1,_,j,_,n}.
# Ejemplo: N(10) devolveria una lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
def N(cantidad):
    NN = []
    for i in range(cantidad):
        NN += [i+1]
    return NN


# Funcion xj.
# Toma un natural n y un intervalo de valores aleatorios entre el
# inf(intervalo) y sup(intervalo) o un eje X, generando N valores
# valore aleatorios entre el inf y el sup
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
    plt.plot(Nn, xji, '*',color = 'black')
    plt.plot(Nn, xji, label="Valores aleatorios", color = 'green')
    plt.title("Grafico de "+str(n)+" valores aleatorios \n entre $-1$ y $1$")
    plt.xlabel("$N$-esimo valor")
    plt.ylabel("Valores generados")
    plt.legend()
    plt.show()

###########################################################################################################
# Definir parametros extras

# Funcion sigma
# calcula la funcion sigma y su derivada para cualquier orden
def sigma(s, orden):
    if orden == 0:
        #print('dsen = sen(s) <=> dsen = sen('+str(s)+') = '+str(np.sin(s)))
        return np.sin(s)
    elif orden == 1:
        #print('dsen = cos(s) <=> dsen = cos('+str(s)+') = '+str(np.cos(s)))
        return np.cos(s)
    elif orden == 2:
        #print('dsen = -sen(s) <=> dsen = -sen('+str(s)+') = '+str(-1*np.sin(s)))
        return -np.sin(s)
    elif orden == 3:
        #print('dsen = -cos(s) <=> dsen = -cos('+str(s)+') = '+str(-1*np.cos(s)))
        return -np.cos(s)


def R_phi(Phi, x, orden):
    w1, w2, b1, b2 = Phi
    if orden == 0:
        return w2 * np.sin(b1 + w1 * x) + b2
    elif orden == 1:
        return w1 * w2 * np.cos(b1 + w1 * x)
    elif orden == 2:
        return -w2 * np.sin(b1 + w1 * x) * w1 * w1


def Gradiente_Rphi(Phi, x, nnabla):
    w1, w2, b1, b2 = Phi
    if nnabla == 1:
        dw1 = w2 * x * np.cos(b1 + w1 * x)
        dw2 = np.sin(b1 + w1 * x)
        db1 = w2 * np.cos(b1 + w1 * x)
        db2 = 1
        grad1 = np.array([dw1, dw2, db1, db2])
        return grad1
    elif nnabla == 2:
        d2w1 = -2 * w1 * w2 * np.sin(b1 + w1 * x) - w2 * x * np.cos(b1 + w1 * x) * (w1 ** 2)
        d2w2 = -np.sin(b1 + w1 * x) * (w1 ** 2)
        d2b1 = -w2 * np.cos(b1 + w1 * x) * (w1 ** 2)
        d2b2 = 0
        grad2 = np.array([d2w1, d2w2, d2b1, d2b2])
        return grad2


def C_phi(Phi, D):
    N = len(D)

    def Coste_C1(D):
        pi2 = (np.pi ** 2) / 4
        C1 = 0
        for i in range(N):
            R2 = R_phi(Phi, D[i], 2)
            R = R_phi(Phi, D[i], 0)
            C1 += (R2 + pi2 * R) ** 2
        return C1

    def Coste_C2(Phi):
        U_1 = (R_phi(Phi, -1, 0)) ** 2
        U1 = (R_phi(Phi, 1, 0)) ** 2
        U0 = (R_phi(Phi, 0, 0) - 1) ** 2
        C2 = U_1 + U1 + U0
        return C2

    Costo1 = (1 / N) * Coste_C1(D)
    Costo2 = (1 / 3) * Coste_C2(Phi)
    Costo = (1 / 2) * (Costo1 + Costo2)
    return Costo


def Parcial(Phi, D, costo):
    if costo == 1:
        R2 = R_phi(Phi, D, 2)
        R = R_phi(Phi, D, 0)
        pi2 = (np.pi ** 2) / 4
        CR = 2 * (R2 + pi2 * R)
        Cc = Gradiente_Rphi(Phi, D, 1)
        parcial = (Cc + pi2 * Cc)
        dC1 = CR * parcial
        grad1 = (dC1[0], dC1[1], dC1[2], dC1[3])
        return grad1
    elif costo == 2:
        CU_1 = 2 * (R_phi(Phi, -1, 0))
        CU1 = 2 * (R_phi(Phi, 1, 0))
        CU0 = 2 * (R_phi(Phi, 0, 0) - 1)
        dCU_1 = Gradiente_Rphi(Phi, -1, 1)
        dCU1 = Gradiente_Rphi(Phi, 1, 1)
        dCU0 = Gradiente_Rphi(Phi, 0, 1)
        parcial1 = CU_1 * dCU_1
        parcial2 = CU1 * dCU1
        parcial3 = CU0 * dCU0
        dC2 = parcial1 + parcial2 + parcial3
        grad2 = ((1 / 3) * dC2[0], (1 / 3) * dC2[1], (1 / 3) * dC2[2], (1 / 3) * dC2[3])
        return grad2


def derivadaParcial(Phi, D, gradn):
    N = len(D) + 1
    if N == 1:
        return gradn
    else:
        datos = D[1:N]
        return derivadaParcial(Phi, datos, gradn=gradn + [Parcial(Phi, D[0], 1)])


def Grad_C1(Phi, D):
    datos = derivadaParcial(Phi, D, gradn=[])
    dw1 = dw2 = db1 = db2 = 0
    for i in range(len(datos)):
        dw1 += datos[i][0]
        dw2 += datos[i][1]
        db1 += datos[i][2]
        db2 += datos[i][3]
    dcostox = [(1 / len(D)) * dw1, (1 / len(D)) * dw2, (1 / len(D)) * db1, (1 / len(D)) * db2]
    dcosto1 = np.array([dcostox])
    return dcosto1


def Grad_C2(Phi, D):
    dcosto2 = np.array([Parcial(Phi, D, 2)])
    return dcosto2


def Gradiente_Cphi(Phi, D):
    gradiente_C1 = Grad_C1(Phi, D)
    gradiente_C2 = Grad_C2(Phi, D)
    DCC = (1 / 2) * (gradiente_C1 + gradiente_C2)
    gradC = [DCC[0, 0], DCC[0, 1], DCC[0, 2], DCC[0, 3]]
    return gradC


def Gradiente_Conjugado(M, l, Phi0, D, a=1):
    w1, w2, b1, b2 = Phi0
    for _ in range(M):
        grad_w1, grad_w2, grad_b1, grad_b2 = Gradiente_Cphi((w1, w2, b1, b2), D)
        w1 += -l * grad_w1
        w2 += -l * grad_w2
        b1 += -l * grad_b1
        b2 += -l * grad_b2
        a = a + 1
    return w1, w2, b1, b2


nu = 0.01
M1 = 100
M2 = 500
M3 = 1000
W = 0.5, 1.1, 1.3, 0

OX = np.linspace(-1, 1, 500)

Gradientes = 'si'
if Gradientes == 'si':
    Caso_M100 = Gradiente_Conjugado(M1, nu, W, xji)
    print(Caso_M100)

    Caso_M500 = Gradiente_Conjugado(M2, nu, W, xji)
    print(Caso_M500)

    Caso_M1000 = Gradiente_Conjugado(M3, nu, W, xji)
    print(Caso_M1000)

    gradM1 = []
    gradM2 = []
    gradM3 = []
    B_x = []
    Cot_sup = []
    Cot_inf = []
    for croissant in range(len(OX)):
        gradM1 += [R_phi(Caso_M100, OX[croissant], 0)]
        gradM2 += [R_phi(Caso_M500, OX[croissant], 0)]
        gradM3 += [R_phi(Caso_M1000, OX[croissant], 0)]
        B_x += [B(OX[croissant])]
        Cot_sup += [1]
        Cot_inf += [-1]

    plt.figure(figsize=(7, 5))
    plt.plot(OX, gradM1, label='$\mathcal{R}(\Phi)(x)_{' + str(M1) + '}$', color='purple')
    plt.plot(OX, gradM2, label='$\mathcal{R}(\Phi)(x)_{' + str(M2) + '}$', color='blue')
    plt.plot(OX, gradM3, label='$\mathcal{R}(\Phi)(x)_{' + str(M3) + '}$', color='green')
    plt.plot(OX, B_x, label='$B(x) = \cos(\\frac{\pi}{2} x)$', color='red')
    plt.plot(OX, Cot_sup, color='gray')
    plt.plot(OX, Cot_inf, color='gray')
    plt.legend(loc='best')
    plt.title('$\mathcal{R}(\Phi)(x)$ para distintos M', fontsize=15)
    plt.xlabel('$x$')
    plt.ylabel('$\mathcal{R}(\Phi)(x)$')
    plt.grid(True)
    plt.show()
