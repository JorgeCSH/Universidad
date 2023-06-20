# Este literal es un codigo para hacer matraca  ############################################################
############################################################################################################
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.abc import a,s,t, N, j
############################################################################################################

x, w1, w2, b1, b2 = sp.symbols('x w1 w2 b1 b2')

R = w2 * sp.sin(w1*x + b1) + b2
C1 = (sp.diff(sp.diff(R, x), x) + ((sp.pi**2)/4)*R)**2
C2 = ((w2*sp.sin(-w1+b1)+b2)**2)+((w2*sp.sin(w1+b1)+b2)**2)+((1-w2*sp.sin(b1)+b2)**2)


dRdx = sp.diff(R, x)


dRdw1 = sp.diff(R, w1)
dRdw2 = sp.diff(R, w2)
dRdb1 = sp.diff(R, b1)
dRdb2 = sp.diff(R, b2)
gradR = np.array([[dRdw1], [dRdw2], [dRdb1], [dRdb2]])


d2Rdx2 = sp.diff(dRdx, x)
d2Rdw1 = sp.diff(d2Rdx2, w1)
d2Rdw2 = sp.diff(d2Rdx2, w2)
d2Rdb1 = sp.diff(d2Rdx2, b1)
d2Rdb2 = sp.diff(d2Rdx2, b2)
gradD2R = np.array([[d2Rdw1], [d2Rdw2], [d2Rdb1], [d2Rdb2]])


dC1dw1 = sp.diff(C1, w1)
dC1dw2 = sp.diff(C1, w2)
dC1db1 = sp.diff(C1, b1)
dC1db2 = sp.diff(C1, b2)
gradC1 = np.array([[dC1dw1], [dC1dw2], [dC1db1], [dC1db2]])

dC2dw1 = sp.diff(C2, w1)
dC2dw2 = sp.diff(C2, w2)
dC2db1 = sp.diff(C2, b1)
dC2db2 = sp.diff(C2, b2)
gradC2 = np.array([[dC2dw1], [dC2dw2], [dC2db1], [dC2db2]])

print('Derivada de R = ', dRdx)
print()
print('Gradiente de R =')
print(gradR)
print()
print('Derivada de R segundo orden = ', d2Rdx2)
print()
print('Gradiente de R segundo orden =')
print(gradD2R)
print()
print('Gradiente de C1 = ')
print(gradC1)
print()
print('Gradiente de C2 = ')
print(gradC2)

def C_phi(Phi, D):
    w1, w2, b1, b2 = Phi
    N = len(D)
    def Coste_C1(D):
        C1 = 0
        for i in range(N):
            R = w2 * np.sin(b1 + w1 * D[i]) + b2
            R2 = -(w1 ** 2) * w2 * np.sin(b1 + w1 * x[i])
            C1 += (R+R2)**2
            #print(i+1)
        return C1
    U_1 = (w2 * np.sin(-w1 + b1) + b2) ** 2
    U1 = (w2 * np.sin(w1 + b1) + b2) ** 2
    U0 = (1 - w2 * np.sin(b1) + b2) ** 2
    Costo2 = (1/3)*(U_1+U1+U0)
    Costo1 = (1/N)*Coste_C1(D)
    Costo = (1/2)*(Costo1+Costo2)
    return Costo
N = 5
(sp.diff(sp.diff(R, x), x) + ((sp.pi**2)/4)*R)**2
