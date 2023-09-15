# Lo hice para calcular los gini
import numpy as np

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


print('Cardinal de valores: ', len(rango_de_valores), len(f_Dhalmar), len(f_francisco), len(f_suizo), len(f_akros), len(f_gaspar), len(f_calasanz))
print("Matriz de f: \n", np.array([f_Dhalmar, f_francisco, f_suizo, f_akros, f_gaspar, f_calasanz]))
print()
N_Dhalmar = []
N_francisco = []
N_suizo = []
N_akros = []
N_gaspar = []
N_calasanz = []
for j in range(len(rango_de_valores)):
    N_Dhalmar += [sum(f_Dhalmar[0:j])]
    N_francisco += [sum(f_francisco[0:j])]
    N_suizo += [sum(f_suizo[0:j])]
    N_akros += [sum(f_akros[0:j])]
    N_gaspar += [sum(f_gaspar[0:j])]
    N_calasanz += [sum(f_calasanz[0:j])]
print("Matriz de N: \n", np.array([N_Dhalmar, N_francisco, N_suizo, N_akros, N_gaspar, N_calasanz]))

def p(lista):
    N = len(lista)
    p = []
    for i in range(N):
        p += [(lista[i]/sum(lista))*100]
    return p

def q(mat_rango, mat_val, rango, val):
    monto_acumulado = np.dot(mat_rango, mat_val)
    q = []
    for i in range(len(rango)):
        q += [(((val[i])*(rango[i]))/monto_acumulado)*100]
    return q
print(p(f_Dhalmar))
def gini(x, y):
    if not len(x) == len(y):
        print("Gil ")
    else:
        for i in range(len(x)):

            pass



