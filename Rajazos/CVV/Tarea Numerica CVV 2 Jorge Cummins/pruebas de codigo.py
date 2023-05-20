# Aca hago pruebas con los codigos
import numpy as np

def phiExtra(w1,w2,b,x0):
    phi = [w1, w2, b, x0]
    return phi
def Rphi(phi):
    w1 = float(phi[0])
    w2 = float(phi[1])
    b = float(phi[2])
    x0 = phi[3]
    x01 = x0[0]
    x02 =x0[1]
    f = (w1*x01+w2*x02+b)
    def sigmoidR(s):
        e = np.exp(s)
        denominador = (1+e)
        sig = e/denominador
        return sig
    ev = sigmoidR(f)
    return ev

def costo(phi):
    rphi = Rphi(phi)






#def gradienteConjugado():

