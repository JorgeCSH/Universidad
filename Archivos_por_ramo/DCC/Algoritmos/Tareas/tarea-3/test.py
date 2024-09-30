
abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
numeros = "0123456789"
operaciones = "+-*/^"

def evaluar_expresion(expresion, dicc_var):
    k = 0
    n = len(expresion)
    resultado = 0
    num_aux = ""
    ultima_operacion = operaciones[0]
    parentesis = 0
    posicion_parentesis_izquierdo = []
    posicion_parentesis_derecho = []
    while k < n:

        if expresion[k] in operaciones:
            if( expresion[0] in '*/^') or ( k >0 and expresion[ k -1] in operaciones) or \
                    (k + 1 < n and expresion[k + 1] in operaciones):
                if k == 0:

                    return (f"ERROR: al procesar {expresion[k]}")
                    # break
                elif expresion[k - 1] in operaciones:
                    return (f"ERROR: al procesar {expresion[k - 1]}")
                    # break
                elif expresion[k + 1] in operaciones:
                    return (f"ERROR: al procesar {expresion[k + 1]}")
                # break

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

        # Realizar las operaciones
        elif expresion[k] in operaciones:
            # Aplicamos el operando al valor actual que pasa a ser valor
            # derecho con el valor anterior a que se encontrara una operacion
            # que originalmente era el resultado
            if num_aux != "":
                valor_izquierdo = resultado
                valor_derecho = num_aux
                valor_izquierdo = aplicar_operacion(valor_izquierdo, valor_derecho, ultima_operacion)
                resultado = valor_izquierdo
            ultima_operacion = expresion[k]
            num_aux = ""

        # Buscamos un parentesis de la forma ( y lo consideramos una
        # expresion que analizaremos por separado
        elif expresion[k] == '(':
            # Buscamos parentesis final
            inicio_parentesis = k + 1
            open_parens = 1
            while open_parens > 0 and k < n - 1:
                k += 1
                if expresion[k] == '(':
                    open_parens += 1
                elif expresion[k] == ')':
                    open_parens -= 1

            fin_parentesis = k
            # De manera recursiva reevaluamos cada uno de los elementos
            expresion_parentesis = evaluar_expresion(expresion[inicio_parentesis:fin_parentesis], dicc_var)

            num_aux = str(expresion_parentesis)
        if expresion[k] == '(':
            posicion_parentesis_izquierdo += [k]
            parentesis += 1
        if expresion[k] == ')':
            parentesis -= 1
            posicion_parentesis_derecho += [k]
        if k == n - 1 and not parentesis == 0:
            return f'ERROR: parentesis no cerrado'

        k += 1

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

    # de llegar al = procesamos
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
