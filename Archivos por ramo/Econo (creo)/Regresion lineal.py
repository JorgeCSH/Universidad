# Informacion ########################################################################################
# Archivo que hice porque soy mus especialito para usar excel
# Este archivo de Python esta hecho para probar, sin embargo intentare que este
# lo mas ordenado posible, pero la idea es que lo incorpore en un notebook para
# hacer mas comodo su uso.

# Imports #############################################################################################
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# Codigo ##############################################################################################
print('# TOP #########################################################################################')
# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3.1, 4.2, 5.3, 6.4])

# Regresion lineal
Coeficientes = np.polyfit(x, y, 1)          # Configurar el tipo de regresion (polinomio grado 1)
a = Coeficientes[0]                         # Pendiente de la ecuacion calculada con la regresion (a)
b = Coeficientes[1]                         # Coeficiente en que fue trasladado (b)


# Valores para OY de la regresion lineal
y_regresion = np.polyval(Coeficientes, x)



# Bosquejo de los datos originales y la regresión lineal
davinci = 'si'
#davinci = 'no'
if davinci == 'si':
    plt.scatter(x, y, label='Datos Utilizados')
    plt.plot(x, y_regresion, color='green', label='Modelo Lineal')
    plt.xlabel('[NOMBRE DE EJE OX]')
    plt.ylabel('NOMBRE DE EJE OY')
    plt.title('[TITULO DEL GRAFICO]')
    plt.legend()
    plt.show()


# Mostrar resultados calculados
print()
print('El modelo sigue una ecuacion dada por: y='+str(a)+'x+'+str(b)+'')
print()
print('Es decir, una ecuacion con: ')
print('Pendiente: '+str(a))
print('Desplazamiento: '+str(b))
print()
print('# Bottom ######################################################################################')
# Creditos ############################################################################################

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


