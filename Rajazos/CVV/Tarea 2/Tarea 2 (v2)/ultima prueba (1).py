# Aca hago pruebas con los codigos
import numpy as np



def sigmoid(s, tipo):
    e = np.exp(s)
    denominador = (1+e)
    if tipo == 0:
        sigmoide = (e)/(denominador)
        return sigmoide
    elif tipo == 1:
        sigmoide = (e)/((denominador)**2)
        return sigmoide



def realizacion(phi, x, dif=0):
    fx = float(phi[0])*float(x[0])+float(phi[1])*float(x[1])+float(phi[2])
    realizar = sigmoid(fx, dif)
    return realizar



def derivadaParcial(phi,dato,tipo):
    for k in range(len(dato)):
        fx = float(phi[0])*float(dato[k][:2][0])+float(phi[1])*float(dato[k][:2][1])+float(phi[2])
        C = sigmoid(fx,0)
        dC = sigmoid(fx,1)
        if tipo == 0:
            dw1 = C*dC*dato[k][0]
            ndato = dw1
            print(ndato)
            return ndato
        elif tipo == 1:
            dw2 = C*dC*dato[k][1]
            ndato = dw2
            print(ndato)
            return ndato
        elif tipo == 2:
            db = C*dC
            ndato = db
            print(ndato)
            return ndato



def dcosto(phi,dif,datos):
    diferencial = []
    for i in range(len(datos)):
        difw1 = [derivadaParcial(phi,datos,0)]
        dw1 = sum(difw1)
        difw2 = [derivadaParcial(phi,datos,1)]
        dw2 = sum(difw2)
        difb = [derivadaParcial(phi,datos,2)]
        db = sum(difb)
        jacobiano = dw1, dw2, db
    if dif == 0:
        return dw1
    elif dif == 1:
        return dw2
    elif dif == 2:
        return db



def gradienteConjugado(k, l, datos):
    w1 = np.random.uniform(-1,1)
    w2 = np.random.uniform(-1,1)
    b = np.random.uniform(-1,1)
    def gradienteFome(w1, w2, b, k, l, datos, a=0):
        if k == 0:
            print(a)
            return [w1, w2, b]
        else:
            w11 = w1 - (l) * float((dcosto([w1, w2, b], 0, datos)))
            w22 = w2 - (l) * float((dcosto([w1, w2, b], 1, datos)))
            bb = b - (l) * float((dcosto([w1, w2, b], 2, datos)))
            w1 = w11
            w2 = w22
            b = bb
            return gradienteFome(w1, w2, b, k - 1, l, datos, a=a+1)
    Cgradiente = gradienteFome(w1, w2, b, k, l, datos)
    return Cgradiente




D = [[9.0, 7.0, 0.0],[2.0, 5.0, 1.0],[3.2, 4.94, 1.0],[9.1, 7.46, 0.0],[1.6, 4.83, 1.0],[8.4, 7.46, 0.0],[8.0, 7.28, 0.0],[3.1, 4.58, 1.0],[6.3, 9.14, 0.0],[3.4, 5.36, 1.0]]
x0 = [8,7]
k = 1000
l = 0.01



phiconjugado = gradienteConjugado(3, l, D)
print("Para la 1000-esima iteracion, vector Phi deberia estar dado por:", phiconjugado)

redrealizada = realizacion(phiconjugado, x0, 0)
print("A su vez, la realizacion estaria dada por:", redrealizada)

#n = 50
#for i in range(n):
#    grad = gradienteConjugado(1000,l,D)
#    print(grad)
#    real = realizacion(grad, X0, 0, 0)
#    print(real)
