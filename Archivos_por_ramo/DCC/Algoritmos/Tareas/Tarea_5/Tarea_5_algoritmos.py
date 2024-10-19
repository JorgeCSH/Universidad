"""Documento que contiene el desarrollo de la tarea 5 de algoritmos.
Enunciado porque me da flojera cambiar de documento.


Un *árbol de búsqueda binaria+* (*ABB+*) es un ABB modificado para que las $n$ llaves que están almacenadas en los nodos internos aparezcan además en las hojas, en orden ascendente,de izquierda a derecha. La última hoja de la derecha tiene una llave especial ``inf``("$+infty$"), como se ve en el siguiente ejemplo:

Para buscar una llave $x$ en este árbol, comenzamos en la raíz y vamos preguntando si $x$ es $le$ que la llave de ese nodo. Si la respuesta es que sí, bajamos hacia la izquierda; si no, bajamos hacia la derecha. Al llegar finalmente a una hoja, ahí se compara por igualdad para ver si la llave buscada está ahí o no.

En comparación con un ABB, el correspondiente ABB+ hace búsquedas más eficientes, porque hace solo una pregunta por nodo, en lugar de las dos que se hacen en el ABB (primero preguntando por igualdad y luego por menor o mayor).

Nótese que un ABB+ vacío (cero llaves) consiste de una sola hoja con ``inf``en su interior.


Objetivos: 

Su trabajo consiste en implementar las clases ``Arbol``, ``Nodoi`` y ``Nodoe`` y los métodos ``insert`` y ``search`` en todos lugares en donde corresponda (no se pide implementar ``delete``). Luego debe ejecutar los casos de prueba que se indica.

Esta tarea se puede resolver con recursividad o sin recursividad. Usted debe decidir cuál enfoque usar.

En el código que aparece a continuación usted debe agregar todo lo necesario para que la implementación esté completa.

"""
# Imports
import aed_utilities as aed
import numpy as np


# Codigo que se implementara
class Nodoi:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der
    
    def search(self, x):
        if x <= self.info:
            return self.izq.search(x)
        else:
            return self.der.search(x)

    def insert(self, x):
        if x <= self.info:
            return Nodoi(self.izq.insert(x), self.info, self.der)
        else:
            return Nodoi(self.izq, self.info, self.der.insert(x))



class Nodoe:
    def __init__(self,info):
        self.info=info
    
    def search(self, x):
        if x <= self.info:
            return self
        else:
            return None
    
    def insert(self, x):
        if x <= self.info:
            return Nodoi(Nodoe(x), self.info, self)
        else:
            return Nodoi(Nodoe(self.info), x, self)

    

class Arbol:
    def __init__(self,raiz=Nodoe(np.inf)):
        self.raiz=raiz

    def search(self, x):
        return self.raiz.search(x)

    def insert(self, x):
        self.raiz=self.raiz.insert(x)

    def dibujar(self):
      btd = aed.BinaryTreeDrawer(fieldData="info", fieldLeft="izq", fieldRight="der", classNone=Nodoe)
      btd.draw_tree(self, "raiz")


# Probar 
def test(a,x):
    print(x, "está" if a.search(x) is not None else "no está")

# Prueba 1
a=Arbol()
a.insert(40)
a.insert(25)
a.insert(32)
a.insert(90)
a.insert(62)
a.insert(55)
a.insert(70)
a.dibujar()
test(a,62)
test(a,95)

# Prueba 2
a.insert(95)
a.dibujar()
test(a,95)




