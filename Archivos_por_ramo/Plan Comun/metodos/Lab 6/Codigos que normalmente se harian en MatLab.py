###################################___Lab 6___###################################
# Librerias usadas
import numpy as np
import  matplotlib.pyplot as plt
##################################################################################
#
# Informacion importante:
# 10000[pF] = 1.0*10^{-8}
# 1[k\Omega] = 1000[\Omega]


intento = input('Inserte numero de intento de realizacion (y de ser necesario, alguna info para diferenciar)  ')
input('Iniciar Parte 1: presiona ENTER ')

# Funcion para interactuar
print('A continuacion Pediran las frecuencias ')
Datos = int(input('Inserte la cantidad de datos '))
if Datos < 0:
    print('Puchale que soi gil ')
    Datos = int(input('Inserte la cantidad de datos '))
elif Datos == 0:
    print('Momento XD ')
# Meterle datos
def Cotorra(cant, valorL, i=0):
    cantidad = int(cant)
    valor = []
    while not cantidad == 0:
        numero = int(input('Dato numero '+str(i+1)+' '))
        valorL += valor + [numero]
        return Cotorra(cant-1, valorL, i=i+1)
    else:
        print('Cantidad de datos mostrada: '+str(i))
        return [valorL, i]
OX = Cotorra(Datos, valorL = [])
print('Ahora los datos medidos ')
OY = Cotorra(Datos, valorL = [])
#print(OX)
#print(OY)
# Guardar datos
Almacenes_Paris = open("No es un SSD lamentablemente.txt", "w")
lin = intento
Almacenes_Paris.write('\n'+lin + str(OX) + str(OY))

input('RECUERDA GUARDAR LAS MEDICIONES MANUALMENTE DESPUES DE CADA MEDICION ')

grafico1 = input('Mostrar Grafico?, presione: 2 si es asi, presione ENTER si no ')
if grafico1 == '1':
    plt.figure(figsize=(7,5))
    plt.scatter(OX[0], OY[0], label = "Transferencia medida ")
    plt.semilogx(OX[0], OY[0], label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "green")
    plt.title("Transferencia en funcion de la frecuencia (Logaritmo) ")
    plt.xlabel("Frecuencia $[Hz]$ ")
    plt.ylabel("Transferencia ")
    plt.legend()
    print()
    plt.figure(figsize=(7,5))
    plt.scatter(OX[0], OY[0], label = "Transferencia medida ")
    plt.plot(OX[0], OY[0], label="Transferencia medida ")
    plt.title("Transferencia en funcion de la frecuencia ")
    plt.xlabel("Frecuencia $[Hz]$ ")
    plt.ylabel("Transferencia ")
    plt.legend()
    plt.show()



iintento = input('Inserte numero de intento de realizacion (y de ser necesario, alguna info para diferenciar)  ')
input('Iniciar Parte 1: presiona ENTER ')

# Funcion para interactuar
print('A continuacion Pediran las frecuencias ')
Datos = int(input('Inserte la cantidad de datos '))
if Datos < 0:
    print('Puchale que soi gil ')
    Datos = int(input('Inserte la cantidad de datos '))
elif Datos == 0:
    print('Momento XD ')
# Meterle datos
def Cotorra(cant, valorL, i=0):
    cantidad = int(cant)
    valor = []
    while not cantidad == 0:
        numero = int(input('Dato numero '+str(i+1)+' '))
        valorL += valor + [numero]
        return Cotorra(cant-1, valorL, i=i+1)
    else:
        print('Cantidad de datos mostrada: '+str(i))
        return [valorL, i]
OXx = Cotorra(Datos, valorL = [])
print('Ahora los datos medidos ')
OYy = Cotorra(Datos, valorL = [])
#print(OX)
#print(OY)

input('RECUERDA GUARDAR LAS MEDICIONES MANUALMENTE DESPUES DE CADA MEDICION ')

grafico2 = input('Mostrar Grafico?, presione: 2 si es asi, presione ENTER si no ')
if grafico2 == '2':
    plt.figure(figsize=(7,5))
    plt.scatter(OXx[0], OYy[0], label = "Transferencia medida ")
    plt.loglog(OXx[0], OYy[0], label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "green")
    plt.title("Transferencia en funcion de la frecuencia (doble logaritmica) ")
    plt.xlabel("Frecuencia $[Hz]$ ")
    plt.ylabel("Transferencia ")
    plt.legend()
    print()
    plt.figure(figsize=(7,5))
    plt.scatter(OXx[0], OYy[0], label = "Transferencia medida ")
    plt.plot(OXx[0], OYy[0], label="Transferencia medida ")
    plt.title("Transferencia en funcion de la frecuencia ")
    plt.xlabel("Frecuencia $[Hz]$ ")
    plt.ylabel("Transferencia ")
    plt.legend()
    plt.show()



# Guardar datos
line = iintento
Almacenes_Paris.write('\n'+line + str(OXx) + str(OYy))
Almacenes_Paris.close()
print()
input('RECUERDA GUARDAR LAS MEDICIONES MANUALMENTE DESPUES DE CADA MEDICION ')
print()
print('Gracias, vuelve pronto (ojala no, significa que te echaste el ramo) ')

###################################___Lab 6___###################################
