# Informacion ########################################################################################
######################################################################################################
# Archivo que hice porque soy mus especialito para usar excel
# Este archivo de Python esta hecho para probar, sin embargo intentare que este
# lo mas ordenado posible, pero la idea es que lo incorpore en un notebook para
# hacer mas comodo su uso.
######################################################################################################
# Imports ############################################################################################
######################################################################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
import os
######################################################################################################
# Codigo #############################################################################################
######################################################################################################

# 1. Manipulacion de los datos ######################################################################

# Obtener el archivo que se va a usar
nombre_archivo = input('Inserte el nombre del archivo ')
ubicacion_archivo = os.path.dirname(os.path.abspath(__file__))
archivo_suffer = ubicacion_archivo+'\\'+nombre_archivo
print(archivo_suffer)
# Leer el archivo CSV en un DataFrame de pandas
suffer_leer = pd.read_csv(archivo_suffer)




# 2. Calculos con los datos #######################################################################

# 2.1 Customizacion # 2.2 Regresion #-------------------------------------------------------------

# Columnas de datos
xx = input('Nombre de la columna que corresponde al eje x ')
yy = input('Nombre de la columna que corresponde al eje y ')

# Ejes
NOMBRE_DE_EJE_OX = input('Inserte nombre del eje x ')
NOMBRE_DE_EJE_OY = input('Inserte nombre del eje y ')
TITULO_DEL_GRAFICO = input('Inserte titulo del grafico ')


# 2.2 Regresion #---------------------------------------------------------------------------------

# Obtencion de datos
x, y = suffer_leer[xx], suffer_leer[yy]

# Regresion lineal
Coeficientes = np.polyfit(x, y, 1)  # Configurar el tipo de regresion (polinomio grado 1)
a = Coeficientes[0]  # Pendiente de la ecuacion calculada con la regresion (a)
b = Coeficientes[1]  # Coeficiente en que fue trasladado (b)

# Valores para OY de la regresion lineal
y_regresion = np.polyval(Coeficientes, x)


# 2.3 Resultados y sus graficos # 2.2 Regresion #-------------------------------------------------

# Bosquejo de los datos originales y la regresión lineal
plt.scatter(x, y, label='Datos Utilizados', color = 'grey')
plt.plot(x, y_regresion, color='green', label='Modelo Lineal')
plt.xlabel(NOMBRE_DE_EJE_OX)
plt.ylabel(NOMBRE_DE_EJE_OY)
plt.title(TITULO_DEL_GRAFICO)
plt.legend()
plt.show()

# Mostrar resultados calculados
print()
print('El modelo sigue una ecuacion dada por: y=' + str(a) + 'x+' + str(b) + '')
print()
print('Es decir, una ecuacion con: ')
print('Pendiente: ' + str(a))
print('Desplazamiento: ' + str(b))
print()



######################################################################################################
# Creditos ###########################################################################################
######################################################################################################
#creditos = 'si'
creditos = 'no'
if creditos == 'si':
    print()
    print('# Credits #####################################################################################')
    fecha_actual = date.today()
    fecha_forma_normal = fecha_actual.strftime("%d/%m/%Y")

    print()
    print('Emition date: ', fecha_forma_normal)
    print()
    print('Developer: <Jorge Cummins>')
    print()
    print('Copyleft Jorgitosoft, all rights reserved.')
    print('Designed by Jorgitosoft at Santiago, Chile.')


