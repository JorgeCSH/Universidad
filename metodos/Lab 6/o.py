import numpy as np
import matplotlib.pyplot as plt
#import tocomple as italiano



def T(V, w, r, c, l, tipo, ll):
    if tipo == 'pasa bajo':
        num = V/(np.sqrt(1+((w*r*c)**2)))
        den = V
        T = num/den
        return T
    elif tipo == 'pasa alto':
        num = V/(np.sqrt(1+(1/((w*r*c)**2))))
        den = V
        T = num/den
        return T
    elif tipo == "pasa banda":
        w0 = 1/np.sqrt(l*c)
        den = np.sqrt((r**2)+((l/w)**2)(((w**2)-(w0**2))**2))
        if ll == "inductancia":
            num = w * l
            T = num/den
            return T
        elif ll == "condensador":
            num = 1/(w*c)
            T = num/den
            return T
        elif ll == "resistencia":
            num = r
            T = num / den
            return T
    else:
        print('error de arrastre, no hay puntaje ')
        e = input('Continuar? ')
        if not e:
            return (V, w, r, c, tipo)


frecuencias = [31.8, 100, 250, 500, 750, 1000, 10000, 100000, 250000, 500000, 750000, 1000000, 5000000, 15000000, 25000000]
frec = []
for i in range(len(frecuencias)):
    frec += [frecuencias[i]*2*(np.pi)]

saquenme_de_beauchef1 =[]
saquenme_de_beauchef2 =[]
aa = []
bb = []
numeritos = []
for i in range(len(frec)):
    saquenme_de_beauchef1 += [T(V=2, w = frec[i], r = 1000, c = 0.00000001, l=00, ll=00, tipo='pasa bajo')]
    saquenme_de_beauchef2 += [T(V=2, w = frec[i], r = 1000, c = 0.00000001, l=00,ll=00, tipo='pasa alto')]
    numeritos += [1+i]
    aa += [[str(i)[0:2]+"|", T(V=2, w = frec[i], r = 1000, c = 0.00000001, l=00,ll=00, tipo='pasa bajo')]]
    bb += [[str(i)[0:2]+"|", T(V=2, w = frec[i], r = 1000, c = 0.00000001, l=00,ll=00, tipo='pasa alto')]]
#print(np.array(aa))
#print(np.array(bb))
#print(numeritos)
#print(saquenme_de_beauchef1)
#print(saquenme_de_beauchef2)






# Graficos
grafico1 = '14'
if grafico1 == '1':
    plt.figure(figsize=(7,5))
    plt.scatter(frec, saquenme_de_beauchef1)
    plt.semilogx(frec, saquenme_de_beauchef1, label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "green")
    plt.title( "Transferencia medida en condensador \n Pasa bajo (Logaritmo)")
    plt.xlabel("$\omega RC$ ")
    plt.ylabel("Transferencia (T)")
    plt.legend()
    print()
    plt.figure(figsize=(7,5))
    plt.scatter(frec, saquenme_de_beauchef1)
    plt.plot(frec, saquenme_de_beauchef1, label="Transferencia medida ")
    plt.title("Transferencia medida en condensador \n Pasa bajo ")
    plt.xlabel("$\omega RC$ ")
    plt.ylabel("Transferencia (T)")
    plt.legend()
    plt.show()

grafico2 = '24'
if grafico2 == '2':
    plt.figure(figsize=(7,5))
    plt.scatter(frec, saquenme_de_beauchef2)
    plt.semilogx(frec, saquenme_de_beauchef2, label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "green")
    plt.title("Transferencia medida en resistencia \n Pasa alto (Logaritmo) ")
    plt.xlabel("$\omega RC$ ")
    plt.ylabel("Transferencia ")
    plt.legend()
    print()
    plt.figure(figsize=(7,5))
    plt.scatter(frec, saquenme_de_beauchef2)
    plt.plot(frec, saquenme_de_beauchef2, label = "Transferencia medida ")
    plt.title("Transferencia medida en resistencia \n Pasa alto ")
    plt.xlabel("$\omega RC$ ")
    plt.ylabel("Transferencia (T)")
    plt.legend()
    plt.show()

grafico3 = '36'
if grafico3 == '3':
    plt.figure(figsize=(7,5))
    plt.scatter(frec, saquenme_de_beauchef2)
    plt.semilogx(frec, saquenme_de_beauchef2, label="Ajuste Logaritmo base 10 ($Log_{10}$)")
    plt.scatter(frec, saquenme_de_beauchef1)
    plt.semilogx(frec, saquenme_de_beauchef1, label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "dracula")
    plt.title("Transferencia en funcion de la frecuencia (Logaritmo) ")
    plt.xlabel("Frecuencia $[Hz]$ ")
    plt.ylabel("Transferencia (T)")
    plt.legend()
    print()
    plt.figure(figsize=(7,5))
    #plt.scatter(frec, saquenme_de_beauchef2, label = "Transferencia medida ")
    plt.plot(frec, saquenme_de_beauchef2, label="Transferencia medida ")
    #plt.scatter(frec, saquenme_de_beauchef1, label = "Transferencia medida ")
    plt.plot(frec, saquenme_de_beauchef1, label="Transferencia medida ")
    plt.title("Transferencia en funcion de la frecuencia ")
    plt.xlabel("$\omega RC$ ")
    plt.ylabel("Transferencia (T)")
    plt.legend()
    plt.show()