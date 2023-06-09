###################################___Lab 6___###################################
# Librerias usadas
import matplotlib.pyplot as plt
##################################################################################
#
# Informacion importante:
# 10000[pF] = 1.0*10^{-8}
# 1[k\Omega] = 1000[\Omega]

# Clase hecha para la el lab

class Davinci:

    # Constructor
    def __init__(self, OX, OY):
        self.OX = OX
        self.OY = OY
        self.nombre_Mediciones = input('Inserte el nombre de la curva ')
        self.nombre_EjeX = input('Inserte nombre del eje OX ')
        self.nombre_EjeY = input('Inserte nombre del eje OY ')
        self.titulo = input('Inserte titulo de la grafica ')
        self.color = input('Inserte Color ')
        self.selector = input('Que tipo de grafico quiere ')


    # Funciones plebeyas

    def dosDimensiones(self):
        if self.selector == '0':
            med = input('Titulo de medicion ')
            plt.figure(figsize=(7, 5))
            plt.scatter(self.OX[0], self.OY[0], label=self.nombre_Mediciones)
            plt.scatter(self.OX[0], self.OY[0], label=med)
            plt.title(self.titulo)
            plt.xlabel(self.nombre_EjeX)
            plt.ylabel(self.nombre_EjeY)
            plt.legend()
            plt.show()
        if self.selector == '1':
            med = input('Titulo de ajuste ')
            plt.semilogx(self.OX[0], self.OY[0], label=med, color=self.color)
            plt.title(self.titulo)
            plt.xlabel(self.nombre_EjeX)
            plt.ylabel(self.nombre_EjeY)
            plt.legend()
            plt.show()
        if self.selector == '2':
            med22 = input('Titulo de ajuste doble logaritmo ')
            plt.loglog(self.OX[0], self.OY[0], label=med22, color=self.color)
            plt.title(self.titulo)
            plt.xlabel(self.nombre_EjeX)
            plt.ylabel(self.nombre_EjeY)
            plt.legend()
            plt.show()



ox = [1,2,3,4,5,6,7,8,9,10]
oy = [1,2,1,33,4,5,6,7,34,4]

o = Davinci(ox, oy)
o1 = Davinci.dosDimensiones(s)