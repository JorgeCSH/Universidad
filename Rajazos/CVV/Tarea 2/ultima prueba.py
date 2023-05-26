import numpy as np


def gradienteConjugado(k, w1, w2, b, l, datos, i=0):
    M = k+1
    w01 = w1
    w02 = w2
    b0 = b
    phix = np.array([[w01], [w02], [b0]])
    while i < M:
        if i == M:
            break
        else:
            w1k = float(phix[i+0-i])-l*costo(phix, 1, 0, datos)
            w2k = float(phix[i+1-i])-l*costo(phix, 1, 1, datos)
            b0k = float(phix[i+2-i])-l*costo(phix, 1, 2, datos)
            w01 = float(w1k)
            w02 = float(w2k)
            b0 = float(b0k)
            phiF = np.array([[w01], [w02], [b0]])
            phix = phiF
            i = i+1
        return phix



def gradienteConjugado(k, w1, w2, b, l, datos):
    M = k+1
    phix = np.array([w1, w2, b])
    for i in range(M):
        w1k = (phix[0,0])-l*costo(np.transpose(phix), 1, 0, datos)
        w2k = (phix[1,0])-l*costo(np.transpose(phix), 1, 0, datos)
        b0k = (phix[2,0])-l*costo(np.transpose(phix), 1, 0, datos)
        phif = np.array([w1k, w2k, b0k])
        phix = phif
        phiF = np.transpose(phix)
        return phiF

def gradienteConjugado(k, w1, w2, b, l, datos):
    M = k+1
    phix = np.array([w1, w2, b])
    for i in range(M):
        w1k = float(phix[0,1])-l*costo(np.transpose(phix), 1, 0, datos)
        w2k = float(phix[0,2])-l*costo(np.transpose(phix), 1, 0, datos)
        b0k = float(phix[0,3])-l*costo(np.transpose(phix), 1, 0, datos)
        phif = np.array([[w1k, w2k, b0k]])
        phix = phif
        phiF = np.transpose(phix)
        return phiF