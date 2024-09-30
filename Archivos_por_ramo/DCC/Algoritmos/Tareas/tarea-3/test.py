# Manually processes and evaluates an expression with parentheses and spaces handled character by character
def evaluar_expresion(expr, dicc_var):
    i = 0
    length = len(expr)
    result = 0
    current_number = ""
    current_operator = '+'

    while i < length:
        char = expr[i]

        # Skip spaces
        if char == ' ':
            i += 1
            continue

        # If it's a digit, accumulate it for the current number
        if char.isdigit():
            current_number += char

        # If it's a letter (variable), get the value from dicc_var
        elif char.isalpha():
            var_name = ""
            while i < length and (expr[i].isalpha() or expr[i].isdigit() or expr[i] == '_'):
                var_name += expr[i]
                i += 1
            i -= 1  # Compensate for extra increment in the loop

            # Lookup the value of the variable in the dictionary
            if var_name in dicc_var:
                current_number = str(dicc_var[var_name])
            else:
                print(f"Error: variable '{var_name}' not defined")
                return 0

        # Handle operators
        elif char in '+-*/^':
            # Apply the previous operator to the current number
            if current_number != "":
                result = aplicar_operacion(result, int(current_number), current_operator)
            current_operator = char
            current_number = ""

        # Handle opening parenthesis '(' by evaluating the sub-expression inside
        elif char == '(':
            # Find the matching closing parenthesis
            sub_expr_start = i + 1
            open_parens = 1
            while open_parens > 0 and i < length - 1:
                i += 1
                if expr[i] == '(':
                    open_parens += 1
                elif expr[i] == ')':
                    open_parens -= 1

            sub_expr_end = i
            # Recursively evaluate the sub-expression
            sub_expr_value = evaluar_expresion(expr[sub_expr_start:sub_expr_end], dicc_var)
            current_number = str(sub_expr_value)

        i += 1

    # Apply the final operation to the last number
    if current_number != "":
        result = aplicar_operacion(result, int(current_number), current_operator)

    return result


# Applies an operation (+, -, *, /, ^) between two numbers
def aplicar_operacion(izq, der, operador):
    if operador == '+':
        return izq + der
    elif operador == '-':
        return izq - der
    elif operador == '*':
        return izq * der
    elif operador == '/':
        return izq // der  # Integer division
    elif operador == '^':
        return izq ** der


# Processes each individual command character by character (no strip used, spaces handled manually)
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

        # Evaluate the expression and store the result in the variable
        dicc_var[var_name] = evaluar_expresion(expr, dicc_var)
        print(f"{var_name} = {expr}")
        print(dicc_var[var_name])

    # If no '=' is present, print the variable value
    else:
        var_name = var_name  # No strip, manually processed
        if var_name in dicc_var:
            print(f"{var_name}")
            print(dicc_var[var_name])
        else:
            print(f"Error: {var_name} not defined.")

    return dicc_var


# Main calculator function (processes a list of commands one by one)
def calculadora(lista_comandos):
    vars = dict()  # Dictionary to store variables
    for comando in lista_comandos:
        if comando != '':  # Ignore empty lines
            vars = procesar_comando(comando, vars)


# Example usage:
lista = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi2 * 2","h2 = hanoi /2","","n"]
calculadora(lista)
