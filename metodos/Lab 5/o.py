import numpy as np
import matplotlib.pyplot as plt
import tocomple as italiano



f = [50, 250, 450, 650, 850, 1050, 1250, 1450, 1650, 1850, 2000]
#periodos = [2.000, 1.998, 1.998, 2.000, 1.999]
perio2 = (2.0000, 0.0005)
emitido = [0.718, 0.716, 0.709, 0.699, 0.686, 0.671, 0.655, 0.636, 0.617, 0.598, 0.583]
emiti2 = [0.559, 0.557, 0.553, 0.547, 0.538, 0.528, 0.515, 0.503, 0.489, 0.474, 0.464]
#px = []
#for i in range(len(periodos)):
#    pe = px+[periodos[i]/(20)]
#    px = pe
    #print(px)

#print('El periodo y su error estan dados por: '+str(2.000)+' ± '+str(0.0005)+'[ms]')
#print('La frecuenca y su error estan dados por: '+str(1/(0.002))+' ± '+str((1/(0.002))*np.sqrt((0.0625))))

purga = -1
if purga == 0:
# grafico sinusoidal
    plt.figure(figsize=(7, 5))
    plt.plot(f, emitido, label = "voltaje", color = "blue")
    plt.title('voltaje vs frecuencia onda sinusoidal')
    plt.xlabel("frecuencia (Hz)")
    plt.ylabel("voltaje ($V$) ")
    plt.legend()
    plt.show()

if purga  == 1:
    # grafico triangular
    plt.figure(figsize=(7, 5))
    plt.plot(f, emiti2, label = "voltaje", color = "blue")
    plt.title('voltaje vs frecuencia onda triangular')
    plt.xlabel("frecuencia (Hz)")
    plt.ylabel("voltaje ($V$) ")
    plt.legend()
    plt.show()

if purga == 2:
    # grafico ambas dos
    plt.figure(figsize=(7, 5))
    plt.plot(f, emitido, label = "voltaje (sinusoidal)", color = "blue")
    plt.plot(f, emiti2, label = "voltaje (triangular)")
    plt.title('voltaje vs frecuencia')
    plt.xlabel("frecuencia (Hz)")
    plt.ylabel("voltaje ($V$) ")
    plt.legend()
    plt.show()

def tau(R,C,L,funador):
    if funador == 0:
        tau = R*C
        return tau
    elif funador == 1:
        tau = L/R
        return tau
print(tau(1000, (10**(-8)), 0.223, 1))


