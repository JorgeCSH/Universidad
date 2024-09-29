"""
Este codigo presenta el desarrollo de la tarea 3 en python en vez de un notebook para ir probando codigos mas
comodamente.
"""

# Esta función recibe un comando en string y el diccionario de variables. Con él,
# procesa el comando, imprime el resultado de la expresion
# y posiblemente modifica el diccionario. La función retorna el diccionario

def procesar_comando(comando, dicc_var):
    # procesa el comando e imprime el resultado
    print(comando)
    val_izquierdo = []
    val_derecho = []
    valores = []
    calc = []
    aux = []
    parentesis_counter = 0
    n = len(comando)
    k = 0
    activador = 0

    # Aca trataremos con el lado "izquierdo" de la expresion
    while k<n:
        # Caso donde en vez de definir una variable se agrega un "="
        if k == 0 and comando[k] == "=":
            resultado = f'ERROR: al procesar "{comando[k]}"'
            print(resultado)
            break

        # Caso donde al definir una variable se tiene un espacio en vez de un "_"
        if comando[k] == " ":
            resultado = f'ERROR: al procesar "{comando[k]}"'
            print(resultado)
            break

        # Caso donde definimos una variable
        if comando[k] == "=":
            # Si despues del "=" no hay nada/no hay espacio o solamente operadores
            if (k==len(comando)-1 or (k==len(comando)-2 and(comando[k+1]==" " or comando[k+1]=="+" or comando[k+1]=="-"
                or comando[k+1]=="*" or comando[k+1]=="/" or comando[k+1]=="^"))):
                resultado = f'ERROR: al procesar "{comando[k]+comando[k+1]}"'
                print(resultado)
                break
            # Caso donde hay algo despues del "=" y tenemos que pasar al lado derecho
            else:
                val_izquierdo += [val_izquierdo[len(val_izquierdo)] + comando[k]]
                valores += [val_izquierdo[len(val_izquierdo)]]
                break

        val_izquierdo += [val_izquierdo[len(val_izquierdo)]+comando[k]]
        # Caso donde el ingresado corresponde a un valor pre ingresado y queremos ver cual es
        if k == len(comando)-1:
            # Si el valor pre ingresado no existe se lanza error
            if not dicc_var[val_izquierdo[len(val_izquierdo)]]:
                resultado = f'ERROR: variable indefinida "{val_izquierdo[len(val_izquierdo)]}"'
                print(resultado)
                break
        # Si tenemos un valor pre ingresado, se printea
        else:
            resultado = f'{val_izquierdo[len(val_izquierdo)]} = {dicc_var[val_izquierdo[len(val_izquierdo)]]}'
            print(resultado)
            break
        valores = [valores[len(valores)]]
        k += 1

    n_2 = n-k
    i = k+1
    # Aca trataremos con el lado derecho de la expresion.
    while i<n_2:
        # Caso donde el lado derecho empieza con error (= extra, *, /, ^)
        if comando[i] == "=" or i == k+1 and (comando[i] == "*" or comando[i] == "/" or comando[i] == "^"):
            resultado = f'ERROR: al procesar "{comando[i]}"'
            print(resultado)
            break

        # Caso donde hay un espacio, recordar que aca ya hay una ecuacion asi que puede permitirse
        if comando[i] == " ":
            val_derecho += [val_derecho[len(val_derecho)]]

        # Parentesis, aca lo agregaremos y les daremos una cuenta para corroborar al final si estan bien o faltan/sobran
        if comando[i] == "(":
            parentesis_counter += 1
            val_derecho += [val_derecho[len(val_derecho)]+comando[i]]
            aux += [val_derecho[len(val_derecho)]]
        if comando[i] == ")":
            parentesis_counter -= 1
            val_derecho += [val_derecho[len(val_derecho)]+comando[i]]
            aux += [val_derecho[len(val_derecho)]]
        if parentesis_counter < 0:
            resultado = f'ERROR: al procesar "{comando[i]}"'
            print(resultado)
            break
        if i == n_2-1 and parentesis_counter != 0:
            resultado = f'ERROR: al procesar parentesis'
            print(resultado)
            break

        # Caso donde el ultimo valor sea alguna operacion
        if i == n_2-1 and (comando[i] == "+" or comando[i] == "-" or comando[i] == "*" or comando[i] == "/" or comando[i] == "^"):
            resultado = f'ERROR: al procesar "{comando[i]}"'
            print(resultado)
            break




    return dicc_var






def calculadora(lista_comandos):
  # Este diccionario almacena las variables que se vayan definiendo en la calculadora
  # Este diccionario se inicializa cuando se usa la calculadora
  vars = dict()

  # Se procesan todos los comandos de la lista (lista de string)
  for i in range(0, len(lista_comandos)):
    vars = procesar_comando(lista_comandos[i], vars)


'''
# EJEMPLO 1:
lista = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi * 2","h2 = hanoi /2","","n"]
calculadora(lista)

'''
