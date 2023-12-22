# Codigo que hice para hacer los graficos en la tarea 8 de economia porque soy muy orgulloso para hacerlo
# de otra forma
import numpy as np
import matplotlib.pyplot as plt


w = np.linspace(0,5,100)

def h(w,t):
    numerador = (w)*1.5*8*(1-t)-3.6*2.5
    denominador = (w+4)*(1-t)*(1.5+3.6)
    oferta = numerador/denominador
    return oferta

def d(T,w,A):
    numerador = (T*A)
    denominador = 2*(w+0.5)
    dd = numerador/denominador
    d = dd**2
    return d

hh = []
h1 = []
h2 = []
h3 = []
dd = []
d1 = []
d2 = []
d3 = []
for i in range(len(w)):
    hh += [h(w[i], 0)]
    h1 += [h(w[i], 0.3)]
    h2 += [h(w[i], 0.85)]
    h3 += [h(w[i], 0.9)]
    dd += [d(1.0, w[i], 1)]
    d1 += [d(1.0, w[i], 1)]
    d2 += [d(2.0, w[i], 1)]
    d3 += [d(3.0, w[i], 1)]

mos = 1
if mos == 1:
    plt.figure(figsize=(7,5))
    #plt.plot(w, dd,label = 'D1', color='red')
    plt.plot(w, d1, label='D1', color='red')
    plt.plot(w, d2, label='D1', color='red')
    plt.plot(w, d3, label='D1', color='red')
    #plt.plot(w, hh, label = 'h', color = "blue")
    plt.plot(w, h1, label = 'h1', color = "blue")
    plt.plot(w, h2, label = 'h2', color = "blue")
    plt.plot(w, h3, label = 'h3', color = "blue")
    plt.title("graficos")
    plt.xlabel("w")
    plt.ylabel("h's")
    plt.legend()
    plt.show()