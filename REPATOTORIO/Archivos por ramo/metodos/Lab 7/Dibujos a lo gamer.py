import numpy as np
import matplotlib.pyplot as plt

opa = np.linspace(-15,15,250)
def Heaviside(x):
    if x<0:
        return 0
    else:
        return 1
doo = []
for i in range(len(opa)):
    doo += [5*np.sin(opa[i])]
print(3.45/np.sqrt(2))
print(0.541/np.sqrt(2))
def rajazitador(t,v):
    matraca = []
    for i in range(len(t)):
        matraca += [-v*np.sin(t[i])*Heaviside(-np.sin(t[i]))]
    return matraca





plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(10, 5))

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
plt.plot(opa, rajazitador(opa, 4.47), label = 'CH2')
plt.plot(opa, doo, label="CH1", color = 'C8')
plt.title("Grafica generada")
ax.set_xlabel("", labelpad=10, loc="right")
ax.set_ylabel("", labelpad=10, loc="top")
plt.legend()

plt.show()


dosd = 'no'
tresd = 'no'
if dosd == 'si':
    plt.figure(figsize=(7, 5))
    plt.plot(opa, np.sin(opa), label="Heaviside")
    plt.plot(opa, opa*0, color =  '0.0')
    plt.title("Funcion de prueba")
    plt.xlabel("$H(x)$")
    plt.ylabel("$x$ ")
    plt.legend()
    plt.show()

if tresd == 'si':
    ax = plt.axes(projection='3d')
    ax.plot_surface(opa, opa, opa, cmap='coolwarm')
    ax.set_title('Forma tridimensional')
    ax.set_xlabel('OX')
    ax.set_ylabel('OY')
    ax.set_zlabel('OZ')
    plt.show()


