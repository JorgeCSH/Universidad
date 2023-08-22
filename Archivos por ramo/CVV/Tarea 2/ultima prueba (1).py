# Aca hago pruebas con los codigos
import numpy as np
import matplotlib.pyplot as plt



def sigmoid(s, tipo):
    e = np.exp(s)
    denominador = (1+e)
    if tipo == 0:
        sigmoide = (e)/(denominador)
        return sigmoide
    elif tipo == 1:
        sigmoide = (e)/((denominador)**2)
        return sigmoide


def f(phi, x):
    (x1, x2) = x
    w1,w2,b = phi
    fx = w1*x1+w2*x2+b
    return fx



def realizacion(phi, x, dif=0):
    gx = f(phi, x)
    gof = sigmoid(gx, dif)
    return gof



def derivadaParcial(phi,datos):
    gradD = []
    for i in range(len(datos)):
        x1d, x2d, xfd = datos[i]
        dato = x1d, x2d
        fx = f(phi,dato)
        C = sigmoid(fx,0)-xfd
        dC = sigmoid(fx,1)
        dw1 = C*dC*x1d
        dw2 = C*dC*x2d
        db = C*dC
        gradx = dw1, dw2, db
        gradd = gradD+[gradx]
        gradD = gradd
        return gradD



def dcosto(phi,datas):
    datos = derivadaParcial(phi,datas)
    dw1 = []
    dw2 = []
    db = []
    for i in range(len(datos)):
        xc1, xc2, xcb = datos[i]
        w1 = dw1 + [xc1]
        dw1 = w1
        w2 = dw2 + [xc2]
        dw2 = w2
        b = db + [xcb]
        db = b
        return [sum(dw1), sum(dw2), sum(db)]



def gradienteConjugado(k, l, datos):
    w1 = np.random.uniform(-1,1)
    w2 = np.random.uniform(-1,1)
    b = np.random.uniform(-1,1)
    def gradienteFome(w1, w2, b, k, l, datos, a=0):
        phi = w1, w2, b
        if k == 0:
            print(a)
            return w1, w2, b
        else:
            w11 = w1 - (l)*float((dcosto(phi, datos)[0]))
            w22 = w2 - (l)*float((dcosto(phi, datos)[1]))
            bb = b - (l)*float((dcosto(phi, datos)[2]))
            w1 = w11
            w2 = w22
            b = bb
            return gradienteFome(w1, w2, b, k - 1, l, datos, a=a+1)
    Cgradiente = gradienteFome(w1, w2, b, k, l, datos)
    return Cgradiente




D = [(9.0,7.0,0.0), (2.0,5.0,1.0), (3.2,4.94,1.0), (9.1,7.46,0.0), (1.6,4.83,1.0), (8.4,7.46,0.0), (8.0,7.28,0.0), (3.1,4.58,1.0), (6.3,9.14,0.0), (3.4,5.36,1.0)]
x0 = (8, 7)
k = 1000
l = 0.01

phiconjugado = gradienteConjugado(980, l, D)
print("Para la 1000-esima iteracion, vector Phi deberia estar dado por:", phiconjugado)

redrealizada = realizacion(phiconjugado, x0, 0)
print("A su vez, la realizacion estaria dada por:", redrealizada)


#n = 50
#for i in range(n):
#    grad = gradienteConjugado(980,l,D)
#    print(grad)
#    real = realizacion(grad, x0, 0)
#    print(real)
