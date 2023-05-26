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
    w01 = w1
    w02 = w2
    b0 = b
    phix = np.array([[w01], [w02], [b0]])
    if  k = 0:
        return phix
    else:
        nw1 = float(phix[0])-(l)*(costo(phix, 1, 0, datos))
        nw2 = float(phix[1])-(l)*(costo(phix, 1, 0, datos))
        nb0 = float(phix[2])-(l)*(costo(phix, 1, 0, datos))
        w1 = nw1
        w2 = nw2
        b = nb0
        return gradienteConjugado(k-1, w1, w2, b, l, datos)



def algoritmo(phi, l, datos):
    nw1 = float(phi[0])-(l)*(costo(phi, 1, 0, datos))
    nw2 = float(phi[1])-(l)*(costo(phi, 1, 1, datos))
    nb0 = float(phi[2])-(l)*(costo(phi, 1, 2, datos))
    return np.array([[nw1], [nw2], [nb0]])


def gradienteConjugado(k, w1, w2, b, l, datos):
    w01 = float(w1)
    w02 = float(w2)
    b0 = float(b)
    phix = np.array([[w01], [w02], [b0]])
    i = 0
    while i < k:
        if i == k:
            break
        else:
            phif = algoritmo(phix, l, datos)
            w1 = phif[0]
            w2 = phif[1]
            b = phif[2]
            philf = gradienteConjugado(k-i, w1, w2, b, l, datos)
            phix = philf
    return phix

