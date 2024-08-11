""""
Corresponde al desarrollo fuera del notebook de la tarea 1, esto para ir probando codigos
y no tener que estar copiando y pegando en el notebook.
"""

# Importar librearias
import numpy as np


# Funciones
"""
print("El orden en que se insertan los equipos es el orden en que se realizan los tiros de penales.")
equipo1 = input("Ingrese el nombre del equipo 1:  ") 
equipo = input("Ingrese el nombre del equipo 2: ")
"""
equipo1 = "Colo Colo"
equipo2 = "U de Chile"


# Funcion muerte subita
def muerte_subita(equipo1, equipo2):
    resultado_subito1 = input("Ingrese resultado del tiro de "+ equipo1+ " ")
    resultado_subito2 = input("Ingrese resultado del tiro de "+ equipo2+ " ")
    if resultado_subito1 == resultado_subito2:
        return muerte_subita(equipo1, equipo2)
    elif resultado_subito1 == "gol":
        print("Gana equipo 1, ", equipo1)
    elif resultado_subito2 == "gol":
        print("Gana equipo 2, ", equipo2)

def tanda_de_penales(equipo1, equipo2):
    caso_ganador11 = (3,0)
    caso_ganador12 = (0,3)
    caso_ganador21 = (4,1)
    caso_ganador22 = (1,4)
    caso_ganador31 = (5,2)
    caso_ganador32 = (2,5)
    contador_equipos = (0,0)
    tiro = 0
    while tiro<3:
        tiro_equipo1 = input("Ingrese resultado del tiro de "+ equipo1+ " ")
        tiro_equipo2 = input("Ingrese resultado del tiro de "+ equipo2+ " ")
        if tiro_equipo1 == "gol":
            contador_equipos += (1,0)
        if tiro_equipo2 == "gol":
            contador_equipos += (0,1)
        tiro = tiro+1


"""    
    if contador_equipo1 == 3 and contador_equipo2 == 0:
        print("Gana equipo 1, ", equipo1)
    elif contador_equipo1 == 0 and contador_equipo2 == 3:
        print("Gana equipo 2, ", equipo2)
    else:
        tiro_equipo12 = input("Ingrese resultado del tiro de " + equipo1 + " ")
        if contador_equipo1 == 3 and contador_equipo2 == 1 and tiro_equipo12 == "gol":
            print("Gana equipo 1, ", equipo1)
        tiro_equipo22 = input("Ingrese resultado del tiro de " + equipo2 + " ")
        if contador_equipo1 == 1 and contador_equipo2 == 3 and tiro_equipo22 == "gol":
            print("Gana equipo 2, ", equipo2)
        else:
            if tiro_equipo1 == "gol":
                contador_equipo1 += 1
            if tiro_equipo2 == "gol":
                contador_equipo2 += 1
            tiro_equipo13 = input("Ingrese resultado del tiro de " + equipo1 + " ")
            if contador_equipo1 == 3 and contador_equipo2 == 1 and tiro_equipo12 == "gol":
                print("Gana equipo 1, ", equipo1)
            tiro_equipo22 = input("Ingrese resultado del tiro de " + equipo2 + " ")
            if contador_equipo1 == 1 and contador_equipo2 == 3 and tiro_equipo22 == "gol":
                print("Gana equipo 2, ", equipo2)"""






'''        tiro_equipo12 = input("Ingrese resultado del tiro de "+ equipo1+ " ")
        tiro_equipo22 = input("Ingrese resultado del tiro de "+ equipo2+ " ")
        if not tiro_equipo12 == tiro_equipo22:
            if tiro_equipo12 == "gol":
                print("Gana equipo 1, ", equipo1)
            elif tiro_equipo22 == "gol":
                print("Gana equipo 2, ", equipo2)
        tiro_equipo13 = input("Ingrese resultado del tiro de "+ equipo1+ " ")
        tiro_equipo23 = input("Ingrese resultado del tiro de "+ equipo2+ " ")
        if not tiro_equipo13 == tiro_equipo23:
            if tiro_equipo13 == "gol":
                print("Gana equipo 1, ", equipo1)
            elif tiro_equipo23 == "gol":
                print("Gana equipo 2, ", equipo2)
            else:
                muerte_subita(equipo1, equipo2)
'''

tanda_de_penales(equipo1, equipo2)





