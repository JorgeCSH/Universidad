abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
numeros = "0123456789"
operaciones = "+-*/^"


# Realizamos las operaciones
def aplicar_operacion(expresion1, expresion2, operador):
    izq = int(expresion1)
    der = int(expresion2)
    assert operador in operaciones
    assert type(izq) == int and type(der) == int
    if operador == '+':
        return int(izq + der)
    elif operador == '-':
        return int(izq - der)
    elif operador == '*':
        return int(izq * der)
    elif operador == '/':
        return int(izq / der)
    elif operador == '^':
        return int(izq ** der)


def simplificar_operaciones(expresion):
    expresion_simplificada = ""
    j = 0
    while j < len(expresion):
        if expresion[j] in '+-' and j + 1 < len(expresion) and expresion[j + 1] in '+-':
            if expresion[j] == '+' and expresion[j + 1] == '+':
                expresion_simplificada += '+'
            elif expresion[j] == '+' and expresion[j + 1] == '-':
                expresion_simplificada += '-'
            elif expresion[j] == '-' and expresion[j + 1] == '+':
                expresion_simplificada += '-'
            elif expresion[j] == '-' and expresion[j + 1] == '-':
                expresion_simplificada += '+'
            j += 1
        else:
            expresion_simplificada += expresion[j]
        j += 1
    return expresion_simplificada


def evaluar_expresion(expresion, dicc_var):
    expresion = simplificar_operaciones(expresion)
    k = 0
    n = len(expresion)
    resultado = 0
    num_aux = ""
    ultima_operacion = operaciones[0]
    while k < n:
        # Caso donde el caracter inicial es una operacion o dos o mas operaciones seguidas que no son posibles
        if expresion[k] in operaciones:
            if k == 0 and expresion[k] in '*/^':
                return(f"ERROR: al procesar {expresion}")
            elif (expresion[k] in '*/^' and ((k > 0 and expresion[k - 1] in '*/^')
                or (k + 1 < n and expresion[k + 1] in '*/^'))):
                if k > 0 and expresion[k - 1] in '*/^':
                    return (f"ERROR: al procesar {expresion[k - 1:]}")
                elif k + 1 < n and expresion[k + 1] in '*/^':
                    return(f"ERROR: al procesar {expresion[k:]}")
            elif k == 0 and expresion[k] in '+-':
                if k + 1 < n and expresion[k + 1] in '*/^':
                    return(f"ERROR: al procesar {expresion[k:]}")
                elif k>0 and expresion[k-1] in '*/^':
                    return(f"ERROR: al procesar {expresion[k-1:]}")
            elif k == n - 1 and expresion[k] in operaciones:
                return (f'ERROR: al procesar "{expresion[k]}"')

        # Caso donde el caracxter de la expresion es un numero.
        if expresion[k] in numeros:
            num_aux += expresion[k]

        # Caso donde el caracter de la expresion es una letra (o un "_")
        elif expresion[k] in abecedario:
            variable = ""
            while k < n and not expresion[k] in operaciones:
                variable += expresion[k]
                k += 1
            k -= 1
            # Vemos si esta precalculada la variable
            if variable in dicc_var:
                num_aux = dicc_var[variable]
            else:
                return f'ERROR: variable indefinida "{variable}"'

        # Calculo de expresiones en parentesis
        elif expresion[k] == '(':
            # Buscamos parentesis final
            inicio_parentesis = k + 1
            parentesis_abierto = 1
            while parentesis_abierto > 0 and k < n - 1:
                k += 1
                if expresion[k] == '(':
                    parentesis_abierto += 1
                elif expresion[k] == ')':
                    parentesis_abierto -= 1
            fin_parentesis = k
            # De manera recursiva reevaluamos cada uno de los elementos
            expresion_parentesis = evaluar_expresion(expresion[inicio_parentesis:fin_parentesis], dicc_var)
            num_aux = str(expresion_parentesis)

        # Calculo de operaciones
        elif expresion[k] in operaciones:
            # Aplicamos el operando al valor actual que pasa a ser valor
            # derecho con el valor anterior a que se encontrara una operacion
            # que originalmente era el resultado
            if num_aux != "":
                resultado = aplicar_operacion(resultado, num_aux, ultima_operacion)
            ultima_operacion = expresion[k]
            num_aux = ""
        k += 1

    # Error asociado al parentesis
    i = 0
    parentesis = 0
    posicion_parentesis_izquierdo = []
    posicion_parentesis_derecho = []
    while i<n:
        if expresion[i] == '(':
            parentesis += 1
            posicion_parentesis_izquierdo = [i]
        elif expresion[i] == ')':
            parentesis -= 1
            posicion_parentesis_derecho = [i]
        i += 1
    if parentesis != 0:
        if posicion_parentesis_izquierdo == []:
            return f'ERROR: al procesar "{expresion[posicion_parentesis_derecho[0]:]}"'
        elif posicion_parentesis_derecho == []:
            return f'ERROR: al procesar "{expresion[posicion_parentesis_izquierdo[0]:]}"'
        elif posicion_parentesis_izquierdo[0] < posicion_parentesis_derecho[0]:
            return f'ERROR: al procesar "{expresion[posicion_parentesis_izquierdo[0]:posicion_parentesis_derecho[len(posicion_parentesis_derecho)-1]]}"'
        elif posicion_parentesis_izquierdo[0] > posicion_parentesis_derecho[0]:
            return f'ERROR: al procesar "{expresion[posicion_parentesis_derecho[0]:posicion_parentesis_izquierdo[len(posicion_parentesis_izquierdo)-1]]}"'

    # Ultimo operador antes de finalizar
    if num_aux != "":
        resultado = aplicar_operacion(resultado, int(num_aux), ultima_operacion)

    return resultado


# Realizamos las operaciones
def aplicar_operacion(expresion1, expresion2, operador):
    izq = int(expresion1)
    der = int(expresion2)
    assert operador in operaciones
    assert type(izq) == int and type(der) == int
    if operador == '+':
        return int(izq + der)
    elif operador == '-':
        return int(izq - der)
    elif operador == '*':
        return int(izq * der)
    elif operador == '/':
        return int(izq / der)
    elif operador == '^':
        return int(izq ** der)


def simplificar_operaciones(expresion):
    expresion_simplificada = ""
    j = 0
    while j < len(expresion):
        if expresion[j] in '+-' and j + 1 < len(expresion) and expresion[j + 1] in '+-':
            if expresion[j] == '+' and expresion[j + 1] == '+':
                expresion_simplificada += '+'
            elif expresion[j] == '+' and expresion[j + 1] == '-':
                expresion_simplificada += '-'
            elif expresion[j] == '-' and expresion[j + 1] == '+':
                expresion_simplificada += '-'
            elif expresion[j] == '-' and expresion[j + 1] == '-':
                expresion_simplificada += '+'
            j += 1
        else:
            expresion_simplificada += expresion[j]
        j += 1
    return expresion_simplificada


# Esta función recibe un comando en string y el diccionario de variables. Con él,
# procesa el comando, imprime el resultado de la expresion
# y posiblemente modifica el diccionario. La función retorna el diccionario
def procesar_comando(comando, dicc_var):
    k = 0
    n = len(comando)
    nombre_variable = ""

    # Separamos el lado izquierdo de la expresion del derecho
    while k < n and comando[k] != '=':
        if comando[k] != ' ':
            nombre_variable += comando[k]
        k += 1

    # Llegamos al punto donde se separa la variable de su expresion
    if k < n and comando[k] == '=':
        nombre_variable = nombre_variable
        k += 1
        expresion = ""
        # Separamos los valores del lado derecho de la expresion
        while k < n:
            if comando[k] != ' ':
                expresion += comando[k]
            k += 1

        # Evaluamos el lado derecho de la expresion
        resultado = evaluar_expresion(expresion, dicc_var)
        if type(resultado) == str:  # Caso error
            print(f"{nombre_variable} = {expresion}")
            print(resultado)
        else:
            dicc_var[nombre_variable] = resultado
            print(f"{nombre_variable} = {expresion}")
            print(dicc_var[nombre_variable])

    # Caso donde no se agrego un =
    else:
        nombre_variable = nombre_variable
        if nombre_variable in dicc_var:
            print(f"{nombre_variable}")
            print(dicc_var[nombre_variable])
        else:
            print(f"ERROR: variable indefinida {nombre_variable}.")

    return dicc_var


# Calculadora principal
def calculadora(lista_comandos):
    vars = dict()
    for comando in lista_comandos:
        if comando != '':
            vars = procesar_comando(comando, vars)


# Ejemplo 1:
lista1 = ["n=5", "hanoi=2^n-1", "var_1 = 23 - 13 + hanoi * 2", "h2 = hanoi /2", "", "n"]
calculadora(lista1)
print()


# Ejemplo 2:
print()
lista2 = ["n=5", "hanoi=2^n-1", "var_1 = 23 - 13 + hanoi2 * 2", "h2 = hanoi /2", "", "n"]
calculadora(lista2)
