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

print(f"Resultados\n"
      f"Oficial: {aa(20)}\n"
      f"Matraca: {resultado2(20)}\n"
      f"El resultado esta: {resultado(aa(5), resultado2(5))}")

