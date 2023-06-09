import numpy as np
import matplotlib.pyplot as plt
#import tocomple as italiano
###################################################################################################################
###################################################################################################################
# Lista de valores
# Frecuencias usadas en Hz
frecuencias = [31.8, 100, 250, 500, 750, 1000, 10000, 100000, 250000, 500000, 750000, 1000000, 5000000, 15000000, 25000000]
# Voltaje que media el oscilosciopio de entrada
V_in1 = [2.07, 2.10, 2.08, 2.07, 2.07, 2.07, 2.05, 2.01, 2.07, 2.08, 2.08, 2.05, 2.05, 2.07, 1.99]
V_in2 = [2.07, 2.09, 2.09, 2.06, 2.07, 2.07, 2.07, 2.06, 2.07, 2.08, 2.08, 2.08, 2.06, 2.07, 2.06]
V_in3 = [2.07, 2.07, 2.07, 2.03, 2.08, 2.07, 2.07, 2.05, 2.07, 2.08, 2.08, 2.07, 2.03, 2.03, 2.07]
# Voltaje que media el osciloscopio en la salida
V_out1 = [2.20, 2.28, 2.20, 2.20, 2.20, 2.16, 1.76, 0.52, 0.42, 0.32, 0.30, 0.30, 0.24, 0.28, 0.24]
V_out2 = [0.16, 0.15, 0.16, 0.18, 0.24, 0.22, 0.24, 0.32, 0.48, 0.80, 1.08, 1.30, 1.75, 2.08, 1.92]
V_out3 = [1.12, 1.10, 1.12, 1.10, 1.10, 1.50, 6.50, 0.17, 0.19, 0.16, 0.16, 0.20, 0.17, 0.12, 0.16]
###################################################################################################################
def transferencia(V_in, V_out):
    assert len(V_in) == len(V_out)
    T_w = []
    for i in range(len(V_in)):
        T_w += [(V_out[i])/(V_in[i])]
    return T_w


def tablas(i = 0, j = 0):
    filas = int(input('Inserte cantidad de filas '))
    columnas = int(input('Inserte cantidad de columnas '))
    textosup = []
    textoinf = []
    while i < columnas:
        ejex = input('Nombre columna '+str(i+1)+' ')
        textosup += [ejex]
        i = i+1
    while j < filas:
        ejexx = input('Nombre fila '+str(j+1)+' ')
        textoinf += [ejexx]
        j = j+1
    DIMTAB = [textosup, textoinf]
    ver = input('Ver info de tablas creadas? \n '
                'si => ver \n'
                'no o cualquier tecla => se lo que hago')
    if ver == 'si':
        print('La dimension de la tabla seria: '+str(filas)+'x'+str(columnas))
        print(DIMTAB)
    else:
        print('aja si tu ')
    return DIMTAB
###################################################################################################################
# Mediciones Circuitos
circuito1 = transferencia(V_in1, V_out1)
circuito2 = transferencia(V_in2, V_out2)
circuito3 = transferencia(V_in3, V_out3)

saquenme_de_beauchef1 =[]
saquenme_de_beauchef2 =[]
saquenme_de_beauchef3 =[]
saquenme_de_beauchef4 =[]
saquenme_de_beauchef5 =[]
saquenme_de_beauchef6 =[]
for i in range(len(circuito1)):
    saquenme_de_beauchef1 += [[str(i+1), V_in1[i], V_out1[i], float(str(circuito1[i])[0:3])]]
    saquenme_de_beauchef2 += [[str(i+1), V_in2[i], V_out2[i], float(str(circuito2[i])[0:3])]]
    saquenme_de_beauchef3 += [[str(i+1), V_in3[i], V_out3[i], float(str(circuito3[i])[0:3])]]


###################################################################################################################
###################################### Programa ###################################################################
###################################################################################################################
input('Para iniciar el programa, presione "ENTER" ')
print()
print('Resultados Lab°6 por ahora')
print('Codigo creado por <autismus_prime69>, derechos reservados')
print()
print()
print('A continuacion se ejecutaran una serie de codigos los cuales pueden ser \n'
      'accesibles si se escribe "si" explicitamente cuando solicitado. Si bien no es necesario \n'
      'escribir nada si no se desea tener acceso, basta con presionar "ENTER" para omitir.')
print()
input('Presione "ENTER" para comenzar ')
mostrar = input('Mostrar resultados por ahora sobre la realizacion? ')
if mostrar == 'si':
    print()
    a = input('Mostrar resultados circuito 1? ')
    if a == 'si':
        # Resultados por circuito
        # Primer circuito
        # Tablas de resultados
        fig, ax = plt.subplots()
        tabla = ax.table(colColours=['gray', 'gray', 'gray', 'gray'], colLabels=['n°', '$Volt_{in}$', "$Volt_{out}$", "Transferencia ($T$)"], cellText=saquenme_de_beauchef1, loc='center', cellLoc='center')
        tabla.auto_set_font_size(True)
        tabla.set_fontsize(12)
        tabla.scale(1, 1.5)
        ax.axis('off')
        plt.show()
        # Graficos
        grafico1 = input('Mostrar Grafico Roberto Carlos? (con arreglo) ')
        if grafico1 == 'si':
            plt.figure(figsize=(7,5))
            plt.semilogx(frecuencias, circuito1, label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "green")
            plt.title( "Transferencia medida en condensador \n Pasa bajo (Logaritmo)")
            plt.xlabel("Frecuencia ($Hz$) con arreglo logaritmico ")
            plt.ylabel("Transferencia (T)")
            plt.legend()
            plt.show()
            gg = input('Mostrar Grafico Roberto Carlos? (sin arreglo) ')
            if gg == 'si':
                plt.figure(figsize=(7,5))
                plt.scatter(frecuencias, circuito1, color = 'black')
                plt.plot(frecuencias, circuito1, label="Transferencia medida ")
                plt.title("Transferencia medida en condensador \n Pasa bajo (sin arreglo)")
                plt.xlabel("Frecuencia ($Hz$) ")
                plt.ylabel("Transferencia (T)")
                plt.legend()
                plt.show()

    input('"ENTER" para continuar ')
    print()
    b = input('Mostrar resultados circuito 2? ')
    if b == 'si':
        # Segundo circuito
        # Tablas de resultados
        fig, ax = plt.subplots()
        tabla = ax.table(colColours=['gray', 'gray', 'gray', 'gray'], colLabels=['n°', '$Volt_{in}$', "$Volt_{out}$", "Transferencia ($T$)"], cellText=saquenme_de_beauchef2, loc='center', cellLoc='center')
        tabla.auto_set_font_size(True)
        tabla.set_fontsize(12)
        tabla.scale(1, 1.5)
        ax.axis('off')
        plt.show()
        # Graficos
        grafico2 = input('Mostrar Grafico Cristiano Ronaldo? (con arreglo) ')
        if grafico2 == 'si':
            plt.figure(figsize=(7,5))
            plt.semilogx(frecuencias, circuito2, label="Ajuste Logaritmo base 10 ($Log_{10}$)", color = "green")
            plt.title( "Transferencia medida en condensador \n Pasa bajo (Logaritmo)")
            plt.xlabel("Frecuencia ($Hz$) con arreglo logaritmico ")
            plt.ylabel("Transferencia (T)")
            plt.legend()
            plt.show()
            gg = input('Mostrar Grafico Cristiano Ronaldo? (sin arreglo) ')
            if gg == 'si':
                plt.figure(figsize=(7,5))
                plt.scatter(frecuencias, circuito2, color = 'black')
                plt.plot(frecuencias, circuito2, label="Transferencia medida ")
                plt.title("Transferencia medida en condensador \n Pasa bajo (sin arreglo)")
                plt.xlabel("Frecuencia ($Hz$) ")
                plt.ylabel("Transferencia (T)")
                plt.legend()
                plt.show()

    input('"ENTER" para continuar ')
    print()
    c= input('Mostrar resultados circuito 3? ')
    if c == 'si':
        # Tercer circuito
        # Tablas de resultados
        fig, ax = plt.subplots()
        tabla = ax.table(colColours=['gray', 'gray', 'gray', 'gray'], colLabels=['n°', '$Volt_{in}$', "$Volt_{out}$", "Transferencia ($T$)"], cellText=saquenme_de_beauchef3, loc='center', cellLoc='center')
        tabla.auto_set_font_size(True)
        tabla.set_fontsize(12)
        tabla.scale(1, 1.5)
        ax.axis('off')
        plt.show()
        # Graficos
        grafico2 = input('Mostrar Grafico caso pasa Bandas (Ojala de metal xd)? (con arreglo) ')
        if grafico2 == 'si':
            plt.figure(figsize=(7,5))
            plt.loglog(frecuencias, circuito3, label="Medicion Inductancia, Arreglo aplicado", color = "green")
            #plt.loglog(frecuencias, Ojala_de_metal, label="Medicion Resistencia, Arreglo aplicado", color = "blue")
            #plt.loglog(frecuencias, Ojala_de_metal, label="Medicion Condensador, Arreglo aplicado", color = "red")
            plt.title( "Transferencia medida en Inductancia \n Pasa Bandas (doble Logaritmo)")
            plt.xlabel("Frecuencia ($Hz$) sin arreglo")
            plt.ylabel("Transferencia (T)")
            plt.legend()
            plt.show()
            gg = input('Mostrar Grafico caso pasa Bandas (Ojala de metal xd)? (sin arreglo) ')
            if gg == 'si':
                plt.figure(figsize=(7, 5))
                plt.scatter(frecuencias, circuito3, '*', color='purple')
                #plt.scatter(frecuencias, Ojala_de_metal, '*', color='purple')
                #plt.scatter(frecuencias, Ojala_de_metal, '*', color='purple')
                plt.plot(frecuencias, circuito3, label="Medicion Inductancia", color="green")
                #plt.plot(frecuencias, Ojala_de_metal, label="Medicion Resistencia", color="blue")
                #plt.plot(frecuencias, Ojala_de_metal, label="Medicion Condensador", color="red")
                plt.title("Transferencia medida en condensador \n Pasa Bandas ")
                plt.xlabel("Frecuencia ($Hz$) sin arreglo")
                plt.ylabel("Transferencia (T)")
                plt.legend()
                plt.show()
print()
input('Presione "ENTER" para salir')
print()
print()
print()
print('Copyright Jorgitosoft, all rights reserved')
print('Software developed by Jorgitosoft at 335 East Sand Hill Road Silicon Valley, California')

