""""
Corresponde al desarrollo fuera del notebook de la tarea 1, esto para ir probando codigos
y no tener que estar copiando y pegando en el notebook.
"""

# Importar librearias
#import numpy as np


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

def tanda_de_penales(equipo1, equipo2, trix=5):
    tiro = 0
    tiros_iniciales = trix-1
    tiros_restantes = tiros_iniciales-tiro
    contador_equipo1 = 0
    contador_equipo2 = 0
    while tiro<5:
        tiros_restantes = tiros_iniciales - tiro
        tiro_equipo1 = input("Ingrese resultado del tiro de "+ equipo1+ " ")
        tiro_equipo2 = input("Ingrese resultado del tiro de "+ equipo2+ " ")
        if tiro_equipo1 == "gol":
            contador_equipo1 += 1
        if tiro_equipo2 == "gol":
            contador_equipo2 += 1
        if contador_equipo1 > contador_equipo2+tiros_restantes:
            print("Gana equipo 1, ", equipo1)
            break
        elif contador_equipo2 > contador_equipo1+tiros_restantes:
            print("Gana equipo 2, ", equipo2)
            break
        else:
            tiro = tiro+1
    if tiros_restantes == 1:
        tiro_equipo1 = input("Ingrese resultado del tiro de " + equipo1 + " ")
        tiro_equipo2 = input("Ingrese resultado del tiro de " + equipo2 + " ")
        if tiro_equipo1 == "gol":
            contador_equipo1 += 1
        if tiro_equipo2 == "gol":
            contador_equipo2 += 1
        if contador_equipo1 > contador_equipo2 + tiros_restantes:
            print("Gana equipo 1, ", equipo1)
        elif contador_equipo2 > contador_equipo1 + tiros_restantes:
            print("Gana equipo 2, ", equipo2)
        else:
            muerte_subita(equipo1, equipo2)





tanda_de_penales(equipo1, equipo2)





