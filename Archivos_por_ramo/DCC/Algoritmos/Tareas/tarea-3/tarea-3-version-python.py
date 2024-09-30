"""
Esta tarea consiste en desarrollar una calculadora de expresiones matemáticas al estilo Matlab o Maple, pero con capacidad de procesar un conjunto de comandos bien restringido. Algunos ejemplos de los comandos que acepta y de lo que debe imprimir en la salida van a continuación:

|Entrada (lo que el usuario escribe)   | Salida(lo que imprime el programa)  |
|---|---|
|n=5   | n=5 |
|   | 5 |
|hanoi=2^n-1    |hanoi = 2^n-1  |
|    |31   |
|var_1 = 23 - 13 + hanoi * 2    |var_1 = 23 - 13 + hanoi * 2   |
|    | 82   |
|h2 = hanoi /2   |h2 = hanoi /2 |
|   | 15   |
|var_2 = (2+n)*2   |var_2 = (2+n)*2    |
|   | 14   |
|var_3 = ((1+n)/2 +3)^2   |var_3 = ((1+n)/2 +3)^2   |
|   | 36   |
|n   |n   |
|  | 5   |

A continuación definimos más en detalle lo que se debe implementar:



1.   Cada comando es de la forma "variable=expresión". El efecto es que primero se debe imprimir el comando y luego se debe calcular la expresión de la derecha, guardar el resultado en la variable de la izquierda e imprimir el resultado en la salida. Si se omite desde el "=" hacia adelante (como en el último ejemplo), solo se imprime el valor de la variable. Las variables comienzan con letra y continúan con letras, dígitos y el signo "_".
2.   Los operadores permitidos son "+","-","*", "/", "^".
3.   Solo se trabaja con números enteros y todas las operaciones dan resultado entero (incluyendo la división, que trunca).
4.   Se puede usar paréntesis, y si no los hay, la expresión se evalúa estrictamente de izquierda a derecha. Eso explica el resultado que se obtiene para "var_1", no hay prioridad de operadores. Pueden venir paréntesis anidados (ver ejemplos)

  **Nota**: Se puede optar por el 70% de la nota si se implementa todo lo solicitado salvo el manejo de paréntesis. En este caso, las expresiones se evaluarán estrictamente de izquierda a derecha sin considerar la prioridad de operadores, y no se permitirá el uso de paréntesis en las expresiones.

5.   Si se utiliza una variable que aún no ha sido definida, se debe dar un error

      ERROR: variable indefinida "..."

6.   Si la sintaxis no es correcta, se debe imprimir en la salida un mensaje de la forma

      ERROR: al procesar "..."

      donde el string que se imprime es la parte de la entrada desde el punto del error hacia adelante.


Antes de empezar a escribir código, usted debe dibujar un diagrama de estados que describa la estructura de la entrada. Si le resulta más conveniente, pueden ser varios diagramas (por ejemplo, uno que describa la estructura de una variable, otro la de un número, otra la de un comando). Luego, a partir de ahí escriba el código que implementa esos diagramas. **Importante:** Su código debe ir procesando de un caracter a la vez, para este procesamiento no se puede utilizar funciones de Python que operen sobre strings de largo mayor que uno. Se recomienda tener una función que reciba un comando en un string y lo procese, y otra que reciba una lista de comandos y vaya invocando a la función antes mencionada para procesarlos.

Para almacenar los nombres y valores de las variables, está permitido el uso de un diccionario de Python.

En su entrega debe describir brevemente el problema, luego describir la estrategia de solución haciendo referencia a su(s) diagrama(s) de estados, y a continuación el código ejecutable respectivo, agregando todas las explicaciones necesarias para que se entienda.
"""


# Esta función recibe un comando en string y el diccionario de variables. Con él,
# procesa el comando, imprime el resultado de la expresion
# y posiblemente modifica el diccionario. La función retorna el diccionario
def procesar_comando(comando, dicc_var):
    # procesa el comando e imprime el resultado

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
