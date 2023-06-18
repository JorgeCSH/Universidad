import numpy as np
import matplotlib.pyplot as plt


def Gradiente_Conjugado(M, l, Phi0, D):
    w1, w2, b1, b2 = Phi0
    def gradienteNC(w1, w2, b1, b2, M, l, D, i=0):
        k = M
        Phi = w1,w2,b1,b2
        while i<M:
            if i == M-1:

                return Phi
            else:
                w11 = w1 - (l) * float((Gradiente_Cphi(Phi, D)[0]))
                w22 = w2 - (l) * float((Gradiente_Cphi(Phi, D)[1]))
                b11 = b1 - (l) * float((Gradiente_Cphi(Phi, D)[2]))
                b22 = b2 - (l) * float((Gradiente_Cphi(Phi, D)[3]))
                w1 = w11
                w2 = w22
                b1 = b11
                b2 = b22
                #print(i)
                return gradienteNC(w1, w2, b1, b2, M, l, D, i=i+1)
    Cgradiente = gradienteNC(w1, w2, b1, b2, M+1, l, D)
    return Cgradiente


