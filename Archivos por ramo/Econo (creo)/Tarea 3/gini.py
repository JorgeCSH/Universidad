# Lo hice para calcular los gini
import numpy as np
import matplotlib.pyplot as plt


# Valores asociados a las instituciones
rango_de_valores = [150, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]
mat_valores = np.array(rango_de_valores)
f_Dhalmar = [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 6, 6, 19, 19, 22, 22, 5]
mat_Dhalmar = np.array(f_Dhalmar)
f_francisco = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 3, 3, 3, 8, 0]
mat_francisco = np.array(f_francisco)
f_suizo = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 5, 3, 5, 3, 0]
mat_suizo = np.array(f_suizo)
f_akros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 3, 8, 8, 5, 3, 1]
mat_akros = np.array(f_akros)
f_gaspar = [0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 7, 5, 2, 9, 6, 7, 3]
mat_gaspar = np.array(f_gaspar)
f_calasanz = [0, 0, 0, 0, 0, 1, 2, 0, 4, 5, 16, 16, 22, 22, 10, 8, 4]
mat_calasanz = np.array(f_calasanz)


# Definimos funciones para realizar el calculo
# Obtiene el valor de pi
def p(lista):
    N = len(lista)
    p = []
    for i in range(N):
        p += [(lista[i]/sum(lista))*100]
    return p

# Obtiene el valor de qi
def q(mat_rango, mat_val, rango, val):
    monto_acumulado = np.dot(mat_rango, mat_val)
    q = []
    for i in range(len(rango)):
        q += [(((val[i])*(rango[i]))/monto_acumulado)*100]
    return q

# Obtiene los valores pero acumulando
def acumulador(lista):
    listaaaa = []
    for i in range(len(lista)+1):
        listaaaa += [sum(lista[0:(i)])]
    return listaaaa

# Calcula el coeficiente de gini asociado a los valores p y q
def gini(p, q):
    if not len(p) == len(q):
        print("Gil ")
    else:
        p_q = []
        for i in range(len(p)):
            p_q += [abs(p[i]-q[i])]
        I = (sum(p_q))/(sum(p))
        return I


# Calculos por institucion
# Liceo D'halmar
p_Dhalmar = acumulador((p(f_Dhalmar)))
q_Dhalmar = acumulador((q(mat_valores, mat_Dhalmar, rango_de_valores, f_Dhalmar)))
gini_Dhalmar = gini(p_Dhalmar,q_Dhalmar)

# Colegio Francisco no se cuanto
p_francisco = acumulador((p(f_francisco)))
q_francisco = acumulador((q(mat_valores, mat_francisco, rango_de_valores, f_francisco)))
gini_francisco = gini(p_francisco,q_francisco)

# Colegio Suizo
p_suizo = acumulador((p(f_suizo)))
q_suizo = acumulador((q(mat_valores, mat_suizo, rango_de_valores, f_suizo)))
gini_suizo = gini(p_suizo,q_suizo)

# Colegio Akros
p_akros = acumulador((p(f_akros)))
q_akros = acumulador((q(mat_valores, mat_akros, rango_de_valores, f_akros)))
gini_akros = gini(p_akros,q_akros)

# Colegio Saint Gaspar College
p_gaspar = acumulador((p(f_gaspar)))
q_gaspar = acumulador((q(mat_valores, mat_gaspar, rango_de_valores, f_gaspar)))
gini_gaspar = gini(p_gaspar,q_gaspar)

# Colegio Calasanz
p_calasanz = acumulador((p(f_calasanz)))
q_calasanz = acumulador((q(mat_valores, mat_calasanz, rango_de_valores, f_calasanz)))
gini_calasanz = gini(p_calasanz,q_calasanz)

# Printea los valores, esto en una matriz
print("Los coeficientes de Gini deberian estar dados por: ")
print(np.array([["Liceo D'halmar", gini_Dhalmar], ["Colegio francisco", gini_francisco], ["Colegio suizo", gini_suizo], ["Colegio akros", gini_akros], ["Colegio Gaspar", gini_gaspar], ["Colegio calasanz", gini_calasanz]]))
OX = np.linspace(0, 100, 18)

def mostrar_grafico():
    # Graficos, mismo orden de antes
    plt.figure(figsize=(7,5))
    plt.plot(OX, q_Dhalmar, label = 'Valores de $q$', color = "green")
    plt.plot(OX, p_Dhalmar, label = 'Valores de $p$', color = "magenta")
    plt.scatter(OX, q_Dhalmar, color = "green")
    plt.scatter(OX, p_Dhalmar, color = "magenta")
    plt.title("Curva de Lorentz para el \n ``Liceo Augusto D'halmar''")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.legend()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(OX, q_francisco, label = 'Valores de $q$', color = "green")
    plt.plot(OX, p_francisco, label = 'Valores de $p$', color = "magenta")
    plt.scatter(OX, q_francisco, color = "green")
    plt.scatter(OX, p_francisco, color = "magenta")
    plt.title("Curva de Lorentz para el \n ``Colegio Francisco Encina''")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.legend()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(OX, q_suizo, label = 'Valores de $q$', color = "green")
    plt.plot(OX, p_suizo, label = 'Valores de $p$', color = "magenta")
    plt.scatter(OX, q_suizo, color = "green")
    plt.scatter(OX, p_suizo, color = "magenta")
    plt.title("Curva de Lorentz para el \n ``Colegio Suizo''")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.legend()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(OX, q_akros, label = 'Valores de $q$', color = "green")
    plt.plot(OX, p_akros, label = 'Valores de $p$', color = "magenta")
    plt.scatter(OX, q_akros, color = "green")
    plt.scatter(OX, p_akros, color = "magenta")
    plt.title("Curva de Lorentz para el \n ``Colegio Akros''")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.legend()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(OX, q_gaspar, label = 'Valores de $q$', color = "green")
    plt.plot(OX, p_gaspar, label = 'Valores de $p$', color = "magenta")
    plt.scatter(OX, q_gaspar, color = "green")
    plt.scatter(OX, p_gaspar, color = "magenta")
    plt.title("Curva de Lorentz para el \n `` Saint Gaspar College''")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.legend()
    plt.show()

    plt.figure(figsize=(7,5))
    plt.plot(OX, q_calasanz, label = 'Valores de $q$', color = "green")
    plt.plot(OX, p_calasanz, label = 'Valores de $p$', color = "magenta")
    plt.scatter(OX, q_calasanz, color = "green")
    plt.scatter(OX, p_calasanz, color = "magenta")
    plt.title("Curva de Lorentz para el \n ``Colegio Calasanz''")
    plt.xlabel("OX")
    plt.ylabel("OY")
    plt.legend()
    plt.show()

#mostrar_grafico()

