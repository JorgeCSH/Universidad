# Manually processes and evaluates an expression with parentheses, spaces, and error handling for undefined variables
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
          if( expresion[0] in '*/^') or (k>0 and expresion[k-1] in operaciones) or (k+1<n and expresion[k+1] in operaciones):
              if k==0:
                
                return(f"ERROR: al procesar {expresion[k]}")
                #break
              elif expresion[k-1] in operaciones:
                return(f"ERROR: al procesar {expresion[k-1]}")
                #break
              elif expresion[k+1] in operaciones:
                return (f"ERROR: al procesar {expresion[k+1]}")
               # break

        # Caso donde el caracxter de la expresion es un numero.
        if expresion[k] in numeros:
            num_aux += expresion[k]


        # Caso donde el caracter de la expresion es una letra (o un "_")
        elif expresion[k] in abecedario:
            variable = ""
            k_factor = 0
            while k_factor < n and not expresion[k] in operaciones:
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

        # Handle opening parenthesis '(' by evaluating the sub-expression inside
        elif expresion[k] == '(':
            # Find the matching closing parenthesis
            sub_expr_start = k + 1
            open_parens = 1
            while open_parens > 0 and k < n - 1:
                k += 1
                if expresion[k] == '(':
                    open_parens += 1
                elif expresion[k] == ')':
                    open_parens -= 1

            sub_expr_end = k
            # Recursively evaluate the sub-expression
            sub_expr_value = evaluar_expresion(expresion[sub_expr_start:sub_expr_end], dicc_var)

            num_aux = str(sub_expr_value)
        if expresion[k] == '(':
            posicion_parentesis_izquierdo += [k]
            parentesis +=1
        if expresion[k] == ')':
            parentesis -=1
            posicion_parentesis_derecho += [k]
        if k == n-1 and not parentesis == 0:
            return f'ERROR: parentesis no cerrado'

        k += 1

    # Apply the final operation to the last number
    if num_aux != "":
        resultado = aplicar_operacion(resultado, int(num_aux), ultima_operacion)

    return resultado

# Applies an operation (+, -, *, /, ^) between two numbers
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


# Processes each individual command character by character (handles errors and prints them)
def procesar_comando(comando, dicc_var):
    i = 0
    length = len(comando)
    var_name = ""

    # Parse the variable name manually (left side of '=')
    while i < length and comando[i] != '=':
        if comando[i] != ' ':  # Skip spaces
            var_name += comando[i]
        i += 1

    # If '=' is found, process the expression
    if i < length and comando[i] == '=':
        var_name = var_name  # No strip, we are processing character by character
        i += 1  # Move past '='
        expr = ""

        # Collect the right-hand expression, skipping spaces
        while i < length:
            if comando[i] != ' ':  # Ignore spaces
                expr += comando[i]
            i += 1

        # Evaluate the expression and handle potential errors
        result = evaluar_expresion(expr, dicc_var)
        if isinstance(result, str) and result.startswith("ERROR"):  # If an error message is returned
            print(f"{var_name} = {expr}")
            print(result)
        else:
            dicc_var[var_name] = result
            print(f"{var_name} = {expr}")
            print(dicc_var[var_name])

    # If no '=' is present, print the variable value
    else:
        var_name = var_name  # No strip, manually processed
        if var_name in dicc_var:
            print(f"{var_name}")
            print(dicc_var[var_name])
        else:
            print(f"ERROR: {var_name} not defined.")

    return dicc_var


# Main calculator function (processes a list of commands one by one, handling errors)
def calculadora(lista_comandos):
    vars = dict()  # Dictionary to store variables
    for comando in lista_comandos:
        if comando != '':  # Ignore empty lines
            vars = procesar_comando(comando, vars)

'''
# Example usage:
lista1 = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi * 2","h2 = hanoi /2","","n"]
calculadora(lista1)
print()
print()
lista2 = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi2 * 2","h2 = hanoi /2","","n"]
calculadora(lista2)'''

print('ERROR'[0:5])
