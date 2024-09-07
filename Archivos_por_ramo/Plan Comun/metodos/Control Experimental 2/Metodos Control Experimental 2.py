# Codigo hecho para ser utilizado en el control experimental 2 de "Metodos Experimentales"
# Posee codigos para hacer mas eficaz el calculo
# 100% no chatgpt (creo)

import numpy as np


# Funcion que calcula en base a una forma especifica
# Opcion 0 == suma directa
# Opcion 1 == reciproco de suma de reciprocos
def matracaEquivalente(datos, purgador):
    suma = 0
    if purgador == 0:
        sumaEquivalente = sum(datos)
    elif purgador == 1:
        for i in range(len(datos)):
            sumat = suma + datos[i]**(-1)
            suma = sumat
            sumaEquivalente = (suma)**(-1)
    else:
        sumaEquivalente = 'Error en tipo de purgador'
    return sumaEquivalente



# Funcion que calcula los valores relacionados a la laey de ohm
# Pide datos como el voltaje, resistencia e intensidad
# "multimetro" decide el tipo de valor que se desea calcular
# 0 == voltaje
# 1 == resistencia
# 2 == intensidad
# conexion es el tipo de conexion que presentan el circuito
# 0 == serie
# 1 == paralelo
def leydeOhm(voltaje, resistencia, intensidad, multimetro, conexion):
    if conexion == 0:
        if multimetro == 0:
            Req = matracaEquivalente(resistencia,0)
            voltajeTot = np.average(intensidad)*Req
            calculoTotal = voltajeTot
        elif multimetro == 1:
            vTot = sum(voltaje)
            ResistenciaTotal = vTot/(np.average(intensidad))
            calculoTotal = ResistenciaTotal
        elif multimetro == 2:
            vTot = sum(voltaje)
            Req = matracaEquivalente(resistencia,0)
            intensidadTotal = vTot/Req
            calculoTotal = intensidadTotal
    elif conexion == 1:
        if multimetro == 0:
            Req = matracaEquivalente(resistencia,1)
            inTot = sum(intensidad)
            voltajeTotal = inTot*Req
            calculoTotal = voltajeTotal
        elif multimetro == 1:
            vTot = np.average(voltaje)
            inTot = sum(intensidad)
            resistenciaTotal = vTot/inTot
            calculoTotal = resistenciaTotal
        elif multimetro == 2:
            vTot = np.average(voltaje)
            Req = matracaEquivalente(resistencia,1)
            intensidadTotal = vTot/Req
            calculoTotal = intensidadTotal
    return calculoTotal