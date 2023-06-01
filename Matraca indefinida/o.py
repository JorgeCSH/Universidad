import numpy as np
import matplotlib.pyplot as plt
import tocomple as italiano

f = [50, 250, 450, 650, 850, 1050, 1250, 1450, 1650, 1850, 2000]
periodos = [2000.0, 1998.0, 1998.0, 2000.0, 1999.0]
emitido = [0.718, 0.716, 0.709, 0.699, 0.686, 0.671, 0.655, 0.636, 0.617, 0.598, 0.583]
emiti2 = [0.559, 0.557, 0.553, 0.547, 0.538, 0.528, 0.515, 0.503, 0.489, 0.474, 0.464]

perme = italiano.media(periodos)
perdev = italiano.desvEstandar(periodos, 0)
mediaxxd = italiano.media(emitido)
desviacionxxd = italiano.desvEstandar(emitido, 0)
mediaxd = italiano.media(emiti2)
desviacionxd = italiano.desvEstandar(emiti2, 0)

aino = italiano.operadorError(valor2=[perme, perdev], valor1=[1,0], operacion=4)

print('Error periodo = '+str(perme)+' ± ' +str(perdev)+'[ms]')
print('Error periodo = '+str(perme)[0:6]+' ± ' +str(perdev)[0:5]+'[ms]')
print('Frecuencia y error = '+str((aino[0]))+' ± '+str(aino[1]))
print()
print('Error sinusoidal = '+str(mediaxxd)+' ± ' +str(desviacionxxd)+'[V]')
print('Error triangular = '+str(mediaxd)+' ± ' +str(desviacionxd)+'[V]')
print()
print('Error sinusoidal = '+str(mediaxxd)[0:5]+' ± ' +str(desviacionxxd)[0:5]+'[V]')
print('Error triangular = '+str(mediaxd)[0:5]+' ± ' +str(desviacionxd)[0:5]+'[V]')

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
