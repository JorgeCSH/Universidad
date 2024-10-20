# Este es el archivo mas ordendo donde ire dejando codigos como tal para el ramo de metodos.....
# Lo usare como conejillo de indias para probar mis abusos de notacioes
# A diferencia del original, este busca ser un documento mas organizado, en algun momento (aunque me duela) le 
# cambiare el nombre a las variables, esto con ef fin de que sea un poco mas mejor
############################################################################################################################

############################################################################################################################
# Librerias
# No puede haber un coigo descente sin librerias....(alerta de flojo jeje) 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import math
# import sympy as sym
import tocomple as italiano
import humanistas as lenguaje
############################################################################################################################

####################################################################################################################
# Aca iria info total

#oltajeCondensador = [4.40, 7.25, 8.70, 9.69, 10.22, 10.46, 10.63, 10.72, 10.79, 10.84, 10.86, 10.87]
#voltajeResistencia = [7.46, 4.63, 2.67, 1.55, 0.98, 0.58, 0.35, 0.24, 0.19, 0.13, 0.11, 0.9]
#datos = np.array([voltajeCondensador, voltajeResistencia])
#print(len(voltajeCondensador))
#print(len(voltajeResistencia))
#df_Voltaje = pd.DataFrame({'Tiempo (s)': [ '[0, 5]', '[5, 10]', '[10, 15]', '[15, 20]', '[20, 25]', '[25, 30]', '[30, 35]', '[35, 40]', '[40, 45]', '[45, 50]', '[50, 55]', '[55, 60]'], 'Voltaje Condensador:' :datos[0], 'Voltaje Resistencia':datos[1]})
#print(df_Voltaje)

####################################################################################################################

############################################################################################################################
# Que iria faltando: 
#   1. Orden == Ordenar un poco mas el codigo, carpetas o cosas asi
#   2. Cambiar nombre variables == Por seriedad
#   3. Asserts  == Saber que estaria funcionando y bien o, que me pude mandar un error
#   4. Programa mas interactivo               \
#                - Python codigo              \ == Hacer mas comodo el uso del codigo
#                - Python interfaz (ideal)    \
############################################################################################################################

############################################################################################################################
# Datos y errores, funciones para calcular, operar, relacionar y diferentes tipos de interacciones con datos
# Funcion encargada de realizar operaciones en base a estadistica
# Dos opciones media y desviacion estandar
# para seleccionarlas, elegir un tipo
# tipo == 0 ....... media
# tipo == 1 ....... desviacion{
#           purgador == 1 ......... los datos son toda la poblacion
#           purgador == 2 ......... los datos son una muestra de la poblacion
#                              }
def estadistica(datos, tipo, purgador):
    typo = lenguaje.racista(tipo)
    datomatraqueables = lenguaje.racista(datos)
    laParca = int(purgador)
    if typo == 0:
        stats = italiano.media(datomatraqueables)
    elif typo == 1:
        if laParca == 0:
            stats = italiano.desvEstandar(datomatraqueables, purgador=0)
        elif laParca == 1: 
            stats = italiano. desvEstandar(datomatraqueables, purgador=1)  
    return stats 
        

# Toma dos valores en formato vector numpy los cuales tienen la funcion de ser notacion error
# Esto permite realizar las operaciones respectivas que se encarga la siguiente funcion
# valor 1 y valor 2 son valores respectivos con sus errores
# operacion es el tipo de operacion que quiere realizarse
def operadorError(valor1, valor2, operacion):                                                          
    a = valor1[1]                                                                      
    b = valor2[1]                                                                 
    aa = valor1[0]                                                                      
    bb = valor2[0]                                                                        
    cateto1 = (a)**2                                                                     
    cateto2 = (b)**2                                                                        
    cateta1 = (a/aa)**2                                                                    
    cateta2 = (b/bb)**2                                                                   
    operro1 = np.sqrt(cateto1 + cateto2)                                                    
    operro2 = np.sqrt(cateta1 + cateta2)                                                    
    matraca = lenguaje.erroropera(aa, bb, operro1, operro2, operacion)                      
    return matraca  
############################################################################################################################

############################################################################################################################
# Graficar 


############################################################################################################################

