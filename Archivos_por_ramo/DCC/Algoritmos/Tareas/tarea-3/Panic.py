def procesar_comando(comando, dicc_var):
    return dicc_var

def calculadora(lista_comandos):
    vars = dict()

    for i in range(0, len(lista_comandos)):
        vars = procesar_comando(lista_comandos[i], vars)


# Ejemplo
# Ejemplo 1
lista1 = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi * 2","h2 = hanoi /2","","n"]
calculadora(lista1)

# Ejemplo 2
lista2 = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi2 * 2","h2 = hanoi /2","","n"]
calculadora(lista2)


