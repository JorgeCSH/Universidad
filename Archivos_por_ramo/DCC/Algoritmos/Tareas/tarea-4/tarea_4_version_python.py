"""
Documento para hacer la tarea 4 de algoritmo

Enunciado (porque me da lata abrir el doc. a cada rato):

El objetivo de esta tarea es aprender a procesar la información de árboles que representan fórmulas. Hay muchas cosas
que uno puede hacer con estos árboles, y en esta tarea nos enfocaremos en particular en calcular la derivada de una
fórmula respecto de una variable dada.

Específicamente, el problema es: dado un árbol que representa una fórmula, construir y retornar otro árbol que
representa la derivada de la primera fórmula respecto de una variable dada.

La fórmula se entrega en notación de infijo (normal). En esta fórmula,
los operadores de menor prioridad son la suma (``+``) y la resta (``-``), de igual prioridad entre sí, luego vienen la
multiplicación (``*``) y la división (``/``), también de igual prioridad entre sí, y finalmente el operador de mayor
prioridad es la elevación a potencia (``^``). También se puede usar paréntesis. Para simplificar no usaremos el
operador "menos unario". **Nota importante**: Para no complicar excesivamente las cosas, supondremos que en la
elevación a potencia el exponente no contiene la variable respecto de la cual se está derivando.

A continuación usted encontrará las clases ``Nodoi``, ``Nodoe`` y ``Arbol`` que implementan árboles que representan
fórmulas. La clase ``Arbol`` viene con un constructor que recibe un string como parámetro, el cual contiene una
fórmula, y este constructor se encarga de transformar la fórmula de string a árbol, de modo que usted no necesita
preocuparse de eso. Para simplificar, la fórmula solo podrá contener variables de una sola letra, números de un solo
dígito, y sin espacios.

Usted tiene que implementar para la clase ``Arbol`` y para los nodos una función ``derivada`` que al ser invocada
indicando el nombre de una variable, retorne un árbol que represente la derivada de la fórmula respectiva.

En este enunciado vienen funciones ``derivada`` triviales, que simplemente retornan la misma fórmula, sin derivarla.
Usted debe reemplazarlas por la implementación correcta
"""


# Imports #############################################################################################################
#######################################################################################################################
import numpy as np
import aed_utilities as aed


# Clases/Codigo principal #############################################################################################
#######################################################################################################################
''' Clase Nodoi

Esta clase que venia originalmente con el documentgo esta encargada de los nodos internos. Lo principal es que 
se encarga de las diferentes opciones de operaciones. Esto es de la siguiente manera:

Caso +: 
    -> Sigue el la regla de la suma de derivadas, es decir, la derivada de la suma es la suma de las derivadas. Esto se realiza tomando retornando otro Nodoi donde la rama izquierda corresponde a la derivada de la izquierda del +, la info corresponde al "+" y el lado derecho corresponde a la derivada de la derecha del +.
    -> d(f+g)/dx = df/dx + dg/dx. 

Caso -:
    -> Analogo a la suma.
    -> d(f-g)/dx = df/dx - dg/dx.

Caso *: 
    -> En este caso se aplica la regla del producto. De esta manera se tomara tres nodoi, el primero para el lado izquierdo de la suma donde su lado izquierdo es la derivada de la funcion, la info un producto y el lado derecho la funcion, el lado derecho es analogo pero invirtiendo los lados y el nodo principal corresponde a los dos nodos pero con "+" como info de este nodo.
    -> d(f*g)/dx = (df/dx)*g + f*(dg/dx).

Caso /: 
    -> Analogo al caso "*" solo que tiene la resta y esta todo dividido por el cuadrado del denominador. Basicamente la regla de la division.
    -> d(f/g)/dx = (df/dx*g - f*dg/dx)/(g^2).

Caso ^:
    -> Considerando que en este caso no se tiene potencias con exponente dependiente del valor que se esta derivando (i.e. exponencial), en este caso se aplicara la regla de derivada de polinomios. Es decir, la derivada de x^n es n*x^(n-1), por lo que la derivada de la potencia sera el exponente por la base a la potencia del exponente menos 1. 
    -> d(f^g)/dx = g*f^(g-1)*df/dx, donde g dg/dx = 0 => cte con respecto a la variable que se esta derivando.

En el caso donde no se tenga ningun caso, ocurre que es cte y por ende se retorna el nodoe como cero.
'''
class Nodoi:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der
    def postorden(self):
        self.izq.postorden()
        self.der.postorden()
        print(self.info, end=" ")
    def derivada(self,x):
        if self.info=="+":
            # Derivada de la suma es la suma de las derivadas, entonces el nodo izquierdo sera la derivada del izquierdo y lo mismo con el derecho.
            return Nodoi(self.izq.derivada(x),"+",self.der.derivada(x))
        if self.info=="-":
            # Analogo a la suma.
            return Nodoi(self.izq.derivada(x),"-",self.der.derivada(x))
        if self.info=="*":
            # Este esta mas chistoso, en este caso tenemos que aplicar propiedad del producto, es decir tenemos que la derivada del producto sera en la izquierda derivada izquierda por derecha y a la derecha, izquierda por derivada derecha.
            return Nodoi(Nodoi(self.izq.derivada(x),"*",self.der),"+",Nodoi(self.izq,"*",self.der.derivada(x)))
        if self.info=="/":
            # Aca aplicamos regla de la division, es decir, analogo al producto pero con una resta y dividiendo por el cuadrado del denominador.
            return Nodoi(Nodoi(Nodoi(self.izq.derivada(x),"*",self.der),"-",Nodoi(self.izq,"*",self.der.derivada(x))),"/",Nodoi(self.der,"^",Nodoe("2")))
        if self.info=="^":
            # Aca aplicamos la regla de la potencia, es decir, derivada de x^n es n*x^(n-1), por lo que la derivada de la potencia sera el exponente por la base a la potencia del exponente menos 1.
            return Nodoi(Nodoi(Nodoi(self.der,"*",self.izq),"^",Nodoi(self.der, "-", Nodoe("1")))  , "*", self.izq.derivada("x"))
        # Caso donde es constante retornamos 0.
        return Nodoe("0")


''' Clase Nodoe
La clase corresponde al nodo externo. En este caso se encarga de las derivadas finales, es decir, si son constantes o variables.
La clase tiene dos opciones para entregar, si es variable entonces la derivada que queda es solamente x^1, por ende se retornara 1, cualquier valor extra se encuentra en los nodos internos. EL otro caso corresponde a cuando no es constante, es decir, como nodo externo se retornara 0.
'''
class Nodoe:
    def __init__(self, info):
        self.info=info
    def postorden(self):
        print(self.info, end=" ")
    def derivada(self,x):
        if self.info==x:
            # Derivada de x es 1.
            return Nodoe("1")
        elif self.info != "x":
            # Derivada de x es 0.
            return Nodoe("0")


''' Clase Arbol.

'''
class Arbol:
    def __init__(self,formula):
        if type(formula)!=str: # se supone que viene el árbol ya construído
          self.raiz=formula
          return

        # la fórmula viene en forma de string
        global k
        global s
        s=formula+";" # agregamos una marca de fin de la entrada
        k=0 # indica próximo caracter por procesar

        # definimos funciones para analizar la fórmula
        def expresion(): # retorna puntero a la raíz de un árbol que representa a la fórmula s
            global k
            global s
            a=factor()
            while s[k]=="+" or s[k]=="-":
                op=s[k]
                k+=1
                b=factor()
                a=Nodoi(a,op,b)
            return a

        def factor():
            global k
            global s
            a=termino()
            while s[k]=="*" or s[k]=="/":
                op=s[k]
                k+=1
                b=termino()
                a=Nodoi(a,op,b)
            return a

        def termino():
            global k
            global s
            a=primario()
            if s[k]=="^":
                op=s[k]
                k+=1
                b=termino()
                a=Nodoi(a,op,b)
            return a

        def primario(): # posible constante, variable o formula parentizada
            global k
            global s
            if s[k].isalpha() or s[k].isdigit():
                a=Nodoe(s[k])
                k+=1
                return a
            if s[k]=="(": # fórmula parentizada
                k+=1
                a=expresion()
                if s[k]!=")":
                    print("Error: Falta cierra paréntesis: "+formula[k:])
                    assert False
                k+=1
                return a
            print("Error: Falta variable, número o abre paréntesis: "+formula[k:])
            assert False

        a=expresion()
        if s[k]!=";":
            print("Error: Basura al final de la fórmula: "+formula[k:])
            assert False
        self.raiz=a

    def derivada(self,x):
        return Arbol(self.raiz.derivada(x))


    def dibujar(self):
      btd = aed.BinaryTreeDrawer(fieldData="info", fieldLeft="izq", fieldRight="der",classNone=Nodoe )
      btd.draw_tree(self, "raiz")


# Aca probamos ########################################################################################################
#######################################################################################################################
def probar_derivada(formula,x):
    f=Arbol(formula)
    print("Fórmula original:")
    f.dibujar()
    g=f.derivada(x)
    print("Derivada respecto de "+x+":")
    g.dibujar()


probar_derivada("x+1","x")

probar_derivada("(2*x)^2+a","x")

probar_derivada("(1+y)/(1-y)","y")

