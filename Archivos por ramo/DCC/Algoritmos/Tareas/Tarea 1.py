"""
Corresponde al desarrollo fuera del notebook de la tarea 1, esto para ir probando codigos
y no tener que estar copiando y pegando en el notebook.
"""

# TAREA ORIGINAL, NO BORRAR
# Aca se ingresan los datos de los equipos que se usaran
print("El orden en que se insertan los equipos es el orden en que se realizan los tiros de penales.")
equipo1 = input("Ingrese el nombre del equipo 1: ")
equipo2 = input("Ingrese el nombre del equipo 2: ")
print()



# Funciones
""" Funcion Muerte subita

El proposito de esta funcion es que en caso de que despues de la tanda de 5 penales los equipos queden empatados se 
determine el ganador con una tanda de dos penales, ganando quien anote.

Esta funcion recibe los nombres de los equipos y el puntaje que se tiene hasta el momento, de ahi realiza una tanda 
de una ronda de penales

En caso de que se tenga el mismo para cada equipo despues de los dos tiros, se vuelve a llamar a la funcion.
En caso de que algun equipo gane, se muestra el equipo ganador.
"""
def muerte_subita(equipo1, equipo2, tiro, contador_equipo1, contador_equipo2):
    resultado_subito1 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo1}?: ")
    resultado_subito2 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo2}?: ")
    if resultado_subito1 == "gol":
        contador_equipo1 += 1
    if resultado_subito2 == "gol":
        contador_equipo2 += 1
    if resultado_subito1 == resultado_subito2:
        return muerte_subita(equipo1, equipo2, tiro+1, contador_equipo1, contador_equipo2)
    elif resultado_subito1 == "gol":
        print(f"Resultado final:")
        print(f"{equipo1}: {contador_equipo1}")
        print(f"{equipo2}: {contador_equipo2}")
        print(f"El ganador es: {equipo1}")
    elif resultado_subito2 == "gol":
        print(f"Resultado final:")
        print(f"{equipo1}: {contador_equipo1}")
        print(f"{equipo2}: {contador_equipo2}")
        print(f"El ganador es: {equipo2}")



"""Funcion Tanda de penales

El proposito de esta funcion es realizar el sistema solicitado para la tanda de penales.
 
Recibe el nombre de los dos equipos mas los tiros que se realizaran en la etapa previa a la muerte subita 
(este valor es fijo pero el codigo esta hecho para que pueda cambiarse y realizar la misma operacion con un numero 
distinto de 5).
 
 En caso de quedar en empate, esta funcion llama a la funcion muerte subita.
"""
def tanda_de_penales(equipo1, equipo2, tiros_iniciales=5):
    tiro = 0
    contador_equipo1 = 0
    contador_equipo2 = 0
    ganador = 0
    print(f"{equipo1} comienza primero")
    while tiro<5:
        tiros_restantes = tiros_iniciales - tiro
        tiro_equipo1 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo1}?: ")
        if tiro_equipo1 == "gol":
            contador_equipo1 += 1
        if contador_equipo1 > contador_equipo2+tiros_restantes:
            print("El ganador se decide antes de completar los 5 tiros debido a una ventaja insuperable. ")
            print("Resultado final: ")
            print(f"{equipo1}: {contador_equipo1}")
            print(f"{equipo2}: {contador_equipo2}")
            print(f"El ganador es: {equipo1}")
            ganador += 1
            break
        if contador_equipo2 >= contador_equipo1+tiros_restantes:
            print("El ganador se decide antes de completar los 5 tiros debido a una ventaja insuperable. ")
            print("Resultado final: ")
            print(f"{equipo1}: {contador_equipo1}")
            print(f"{equipo2}: {contador_equipo2}")
            print(f"El ganador es: {equipo2}")
            ganador += 1
            break
        tiro_equipo2 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo2}?: ")
        if tiro_equipo2 == "gol":
            contador_equipo2 += 1
        if contador_equipo2 >= contador_equipo1+tiros_restantes:
            print("El ganador se decide antes de completar los 5 tiros debido a una ventaja insuperable. ")
            print("Resultado final: ")
            print(f"{equipo1}: {contador_equipo1}")
            print(f"{equipo2}: {contador_equipo2}")
            print(f"El ganador es: {equipo2}")
            ganador += 1
            break
        if contador_equipo1 >= contador_equipo2+tiros_restantes:
            print("El ganador se decide antes de completar los 5 tiros debido a una ventaja insuperable. ")
            print("Resultado final: ")
            print(f"{equipo1}: {contador_equipo1}")
            print(f"{equipo2}: {contador_equipo2}")
            print(f"El ganador es: {equipo1}")
            ganador += 1
            break
        tiro = tiro+1
    if ganador == 0:
        print()
        print("Resultado despues de los 5 tiros: ")
        print(f"{equipo1}: {contador_equipo1}")
        print(f"{equipo2}: {contador_equipo2}")
        print("Empate! Vamos a muerte subita")
        print()
        muerte_subita(equipo1, equipo2, tiro, contador_equipo1, contador_equipo2)



# Iniciamos el programa
tanda_de_penales(equipo1, equipo2)


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
"""
print("El orden en que se insertan los equipos es el orden en que se realizan los tiros de penales.")
equipo1 = input("Ingrese el nombre del equipo 1: ")
equipo2 = input("Ingrese el nombre del equipo 2: ")
print()


def muerte_subita(equipo1, equipo2, tiro, contador_equipo1, contador_equipo2):
    resultado_subito1 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo1}?: ")
    resultado_subito2 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo2}?: ")
    equipo_ganador = ""
    while resultado_subito1 == resultado_subito2:
        if resultado_subito1 == "gol" or resultado_subito2 == "gol":
            muerte_subita(equipo1, equipo2, tiro+1, contador_equipo1+1, contador_equipo2+1)
        muerte_subita(equipo1, equipo2, tiro + 1, contador_equipo1, contador_equipo2)
    print(f"Resultado final:")
    if resultado_subito1 == "gol":
        contador_equipo1 += 1
        equipo_ganador = equipo1
    if resultado_subito2 == "gol":
        contador_equipo2 += 1
        equipo_ganador = equipo2
    print(f"{equipo1}: {contador_equipo1}")
    print(f"{equipo2}: {contador_equipo2}")
    print(f"El ganador es: {equipo_ganador}")


def mostrar_ganador(equipo1, equipo2, contador_equipo1, contador_equipo2, ganador_insuperable):
    print("El ganador se decide antes de completar los 5 tiros debido a una ventaja insuperable. ")
    print("Resultado final: ")
    print(f"{equipo1}: {contador_equipo1}")
    print(f"{equipo2}: {contador_equipo2}")
    print(f"El ganador es: {ganador_insuperable}")


def tanda_de_penales(equipo1, equipo2, tiros_iniciales=5):
    tiro = 0
    contador_equipo1 = 0
    contador_equipo2 = 0
    ganador = 0
    print(f"{equipo1} comienza primero")
    while tiro<5:
        tiros_restantes = tiros_iniciales - tiro
        tiro_equipo1 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo1}?: ")
        if tiro_equipo1 == "gol":
            contador_equipo1 += 1
        if contador_equipo1 > contador_equipo2+tiros_restantes:
            mostrar_ganador(equipo1, equipo2, contador_equipo1, contador_equipo2, equipo1)
            ganador += 1
            break
        if contador_equipo2 >= contador_equipo1+tiros_restantes:
            mostrar_ganador(equipo1, equipo2, contador_equipo1, contador_equipo2, equipo2)
            ganador += 1
            break
        tiro_equipo2 = input(f"¿Ingrese resultado de el tiro {tiro+1} del jugador del equipo {equipo2}?: ")
        if tiro_equipo2 == "gol":
            contador_equipo2 += 1
        if contador_equipo2 >= contador_equipo1+tiros_restantes:
            mostrar_ganador(equipo1, equipo2, contador_equipo1, contador_equipo2, equipo2)
            ganador += 1
            break
        if contador_equipo1 >= contador_equipo2+tiros_restantes:
            mostrar_ganador(equipo1, equipo2, contador_equipo1, contador_equipo2, equipo1)
            ganador += 1
            break
        #print(contador_equipo1, contador_equipo2, tiros_restantes)
        tiro = tiro+1
    if ganador == 0:
        print()
        print("Resultado despues de los 5 tiros: ")
        print(f"{equipo1}: {contador_equipo1}")
        print(f"{equipo2}: {contador_equipo2}")
        print("Empate! Vamos a muerte subita")
        print()
        muerte_subita(equipo1, equipo2, tiro, contador_equipo1, contador_equipo2)


tanda_de_penales(equipo1, equipo2)


"""










