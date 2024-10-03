# Imports
import numpy as np
import matplotlib.pyplot as plt

# Corresponde a un archivo para estudiar para el control.

# P2 a) a_{n} = 3a_{n-1}+4a_{n-2}, a_{0} = 2, a_{1} = 3
def a(n):
    a_0 = 2
    a_1 = 3
    a_n = [a_0, a_1]
    if n>=2:
        for i in range(2, n+1):
            a_n += [3*a_1 + 4*a_0]
            N = len(a_n)
            a_0 = a_n[N-2]
            a_1 = a_n[N-1]
        return a_n

def matraca_a(n):
    a_n = []
    for i in range(n+1):
        a_n += [(4**i)+((-1)**i)]
    return a_n

def resultado(a, b):
    if a == b:
        return "Correcto"
    else:
        return "Incorrecto"
'''
print(f"Resultados\n"
      f"Oficial: {a(5)}\n"
      f"Matraca: {matraca_a(5)}\n"
      f"El resultado esta: {resultado(a(5), matraca_a(5))}")
'''

# P2 b) a_{n} = 2a_{n-1}+a_{n-2}, a_{0} = 0, a_{1} = 4
def aa(n):
    a_0 = 0
    a_1 = 4
    a_n = [a_0, a_1]
    if n>=2:
        for i in range(2, n+1):
            a_n += [float(2*a_1 + a_0)]
            N = len(a_n)
            a_0 = a_n[N-2]
            a_1 = a_n[N-1]
        return a_n

def resultado2(n):
    a_n = []
    a = 1
    b = 2**(1/2)
    phi_1 = (1+b)
    phi_2 = (1-b)
    for i in range(n+1):
        a_n += [a*b*(((phi_1)**i)-((phi_2)**i))]
    return a_n
'''
print(f"Resultados\n"
      f"Oficial: {aa(20)}\n"
      f"Matraca: {resultado2(20)}\n"
      f"El resultado esta: {resultado(aa(5), resultado2(5))}")
'''
def lanzarMoneda():
    lado = np.random.randint(0, 2,1)
    lados_posibles = {0: "Sello", 1: "Cara"}
    if lados_posibles[int(lado)] == "Cara":
        return True
    else:
        return False


def juegoConMonedas():
    '''
    Buscamos implementar que gane alicia si sale True True False y Roberto si sale True False False
    cada tiro es recursivo
    '''
    tiro = lanzarMoneda()
    if tiro == True:
        tiro2 = lanzarMoneda()
        if tiro2 == True:
            tiro3 = lanzarMoneda()
            if tiro3 == False:
                return "Gana Alicia"
            else:
                return juegoConMonedas()
        else:
            return "Gana Roberto"
    else:
        return juegoConMonedas()

# P2
def pregunta(n):
    t_1 = 3
    t_2 = 15
    t_n = [t_1, t_2]
    if n>=3:
        for i in range(3, n+1):
            t_n += [5*t_2 - 4*t_1]
            N = len(t_n)
            t_1 = t_n[N-2   ]
            t_2 = t_n[N-1]
        return t_n

def des(n):
    t_n = [3, 15]
    for i in range(3, n+1):
        t_n += [-1+(4**i)]
    return t_n
'''
print(f"Resultados\n"
      f"Oficial: {pregunta(n=5)}\n"
      f"Matraca: {des(n=5)}\n"
      f"El resultado esta: {resultado(pregunta(n=5), des(n=5))}")
'''

# P3
def T_analitica(n):
    T_n = [1, 1]
    for i in range(2, n+1):
        T_n += [2*(3**i)-(5**i)]
    return T_n
#print(T_analitica(5))

def T_inef(n):
    if n <= 1:
        return 1
    else:
        return 8*T_inef(n-1)-15*T_inef(n-2)
ttt = []
for i in range(5+1):
    ttt += [T_inef(i)]

def T_ef(n):
    T = np.zeros(n+1, dtype= int)
    T[0] = 1
    T[1] = 1
    for i in range(2, n+1):
        T[i] = 8*T[i-1]-15*T[i-2]
    return T

print(T_ef(5))