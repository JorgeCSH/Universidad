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
    fx = float(phi[0])*float(dato[:2][0])+float(phi[1])*float(dato[:2][1])+float(phi[2])
    C = sigmoid(fx,0)
    dC = sigmoid(fx,1)
    if tipo == 0:
        dw1 = C*dC*dato[0]
        ndato = dw1
        return ndato
    elif tipo == 1:
        dw2 = C*dC*dato[1]
        ndato = dw2
        return ndato
    elif tipo == 2:
        db = C*dC
        ndato = db
        return ndato



def dcosto(phi,dif,datos):
    diferencial = []
    for i in datos:
        data = datos[i]
        if dif == 0:
            dw1 = diferencial+[derivadaParcial(phi,data,0)]
            diferencial = dw1
            costoRealizacion = sum(diferencial)
            return costoRealizacion
        elif dif == 1:
            dw2 = diferencial+[derivadaParcial(phi,data,1)]
            diferencial = dw2
            costoRealizacion = sum(diferencial)
            return costoRealizacion
        elif dif == 2:
            db = diferencial + [derivadaParcial(phi,data,2)]
            diferencial = db
            costoRealizacion = sum(diferencial)
            return costoRealizacion



def gradienteConjugado(k, l, datos):
    w1 = np.random.uniform(-1,1)
    w2 = np.random.uniform(-1,1)
    b = np.random.uniform(-1,1)
    for j in range(k):
        w1 = w1-(l)*float((dcosto([w1,w2,b],0,datos)))
        w2 = w2-(l)*float((dcosto([w1,w2,b],1,datos)))
        b = b-(l)*float((dcosto([w1,w2,b],2,datos)))
        phix = [w1,w2,b]
        return phix



D = [[9.0, 7.0, 0.0],[2.0, 5.0, 1.0],[3.2, 4.94, 1.0],[9.1, 7.46, 0.0],[1.6, 4.83, 1.0],[8.4, 7.46, 0.0],[8.0, 7.28, 0.0],[3.1, 4.58, 1.0],[6.3, 9.14, 0.0],[3.4, 5.36, 1.0]]
x0 = [8,7]
k = 1000
l = 0.01



# Desarrollo final
#   I. Ejecutar el gradiente para obtener el Phi = (wk1, wk2, bk2)
#   II. Llamando "phi = gradiente conjugado", ejercutamos la
#       realizacion en (8, 7) y phi
#   III. Printeamos n resultados con la cantidad "n", numero natural a gusto
#   IV. Printear punto evaluado inicialmente
# I.
phiconjugado = gradienteConjugado(1000, l, D)                                                  # Aplicacion del gradiente conjugado
print("Para la 1000-esima iteracion, vector Phi deberia estar dado por:", phiconjugado)                  # Mostrar resultados
# II.
#redrealizada = realizacion(phiconjugado, x0, 0)                                                        # Obtencion de red neuronal
#print("A su vez, la realizacion estaria dada por:", redrealizada)                                         # Mostrar resultados
# III.
#n = 50
#for i in range(n):
#    grad = gradienteConjugado(1000,l,D)
    #print(grad)
#    real = realizacion(grad, X0, 0, 0)
#    print(real)
