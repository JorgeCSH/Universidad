# Archivo para realizar la tarea 6 de algoritmos
'''
El objetivo de esta tarea es que usted implemente árboles 2-3. Si ve en el apunte, para los árboles AVL aparece la
implementación, pero no así para los árboles 2-3. Usted debe ayudar a completar el apunte y si lo hace bien, es posible
 que en el futuro aparezca su código en este capítulo.

A continuación aparece algo de código para ayudarlo a partir. Hay dos tipos de nodos internos (``Nodo2`` y ``Nodo3``),
 según si ese nodo es binario o ternario, y un tipo de nodo externo u hoja (``Nodoe``). Además, está la clase
 ``Arbol23``, que es el punto de partida. Las operaciones que usted tiene que implementar son ``insert`` y ``search``.

En varias partes se ha rellenado con código provisorio, para que compile. Usted debe reemplazar y completar todo lo que
sea necesario para que todo funcione.

El código esbozado más abajo está orientado a una implementación recursiva, la que podemos describir de la siguiente
manera:

* Si se inserta una llave en un nodo binario, hay que insertarla recursivamente en el hijo izquierdo o en el derecho,
según corresponda. Si esto no produce un *split* del hijo, el resultado es un puntero al nodo resultante (que puede ser
 binario o ternario), lo cual se anota en el lugar respectivo y se retorna un puntero al nodo resultante. Pero si el
  hijo se divide, se recibe el resultado que es una tupla que contiene el árbol izquierdo, el árbol derecho, y la llave
   que los separa. Con esto este nodo tiene la información para mutar a ternario y retornar el resultado.

* Si se inserta una llave en un nodo ternario hay que insertarla recursivamente en el hijo izquierdo, en el del medio
o en el derecho, según corresponda. Si esto no produce un *split* del hijo, el resultado es un puntero al nodo
resultante (que puede ser binario o ternario), lo cual se anota en el lugar respectivo y se retorna un puntero al nodo
resultante. Pero si el hijo se divide, se recibe el resultado que es una tupla que contiene el árbol izquierdo, el
árbol derecho, y la llave que los separa. Con esto este nodo tiene la información para a su vez dividirse y retornar
la tupla resultante.

* Lo anterior permite modelar de la misma manera la inserción en una hoja: al recibir una llave, se divide en dos
 hojas, y la llave entrante las separa. Esto se retorna hacia arriba en la forma de una tupla y se la da el mismo
 tratamiento anterior.

* En la clase ``Arbol23`` hay que estar preparado para recibir una tupla como resultado de la inserción, lo cual
indicaría que la raíz se dividió. En ese caso, hay que crear nodo binario para que sea la nueva raíz.

La operación de búsqueda (``search``) debe retornar un puntero al nodo que contiene la llave buscada, en caso de ser
exitosa, o ``None`` si es infructuosa
'''

'''
def search(self,x):
    return None # Aquí hay que retornar el resultado de buscar x a partir de este punto
                # Esto puede ser un puntero al nodo en donde está x, o None si no está
'''
'''
def search(self,x):
    return None # Aquí hay que retornar el resultado de buscar x a partir de este punto
                # Esto puede ser un puntero al nodo en donde está, o None si no está
'''


class Nodo2:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der

    def insert(self,x):
        return None # Aquí hay que retornar el resultado de insertar x a partir de este punto

    def search(self,x):
      # Caso donde vemos si el valor buscado es menor al del nodo.
      if x < self.info:
        return self.izq.search(x)

      # Caso donde vemos si el valor buscado es mayor al del nodo.
      elif x > self.info:
        return self.der.search(x)

      # Caso sobrante es y sin error es que sea igual.
      return self


    def string(self):
        return ("("+self.izq.string()
                +str(self.info)
                +self.der.string()+")")

class Nodo3:
    def __init__(self, izq, info1, med, info2, der):
        self.izq=izq
        self.info1=info1
        self.med=med
        self.info2=info2
        self.der=der

    def insert(self,x):
        return None # Aquí hay que retornar el resultado de insertar x a partir de este punto

    def search(self,x):
        # Caso donde x es igual a la llave/info1.
        if x == self.info1:
          return self

        # Caso donde x es igual a la llave/info2.
        elif x == self.info2:
          return self

        # Caso donde es menor que info1, se baja a la izquierda.
        elif x < self.info1:
            return self.izq.search(x)

        # Caso donde es mayot que info2, se baja a la derecha.
        elif x > self.info2:
            return self.der.search(x)

        return self.med.search(x)

    def string(self):
        return ("("+self.izq.string()
                +str(self.info1)
                +self.med.string()
                +str(self.info2)
                +self.der.string()+")")

class Nodoe:
    def __init__(self):
        pass

    def insert(self,x):
        return None # Aquí hay que retornar el resultado de insertar x a partir de este punto

    def string(self):
        return"☐"

    # Metodo provisorio, probablemente reemplazar en el arbol
    def search(self,x):
        return None


class Arbol23:
    def __init__(self,raiz=Nodoe()):
        self.raiz=raiz

    def insert(self,x):
        self.raiz=self.raiz.insert(x)   # Esto funciona casi siempre, excepto cuando la antigua raíz se divide
                                        # Usted tiene que poner algo que funcione siempre

    def search(self,x):
        return self.raiz.search(x)

    def imprimir(self):
        print(self.raiz.string())


# Para probar este código, vamos a construir "a mano" el árbol 2-3 que aparece en el apunte, y luego imprimirlo
a=Nodo3(Nodo2(Nodoe(),10,Nodoe()),25,Nodo3(Nodoe(),32,Nodoe(),48,Nodoe()),57,Nodo2(Nodoe(),74,Nodoe()))
print(a.string())

#print(a.search(25).string())


#((☐10☐)25(☐32☐48☐)57(☐74☐))

'''
Corregir o estar atento
- Por ahora estoy haciendo uso de un metodo que  me saque de la raja, atento.
- Por ahora search es literal lo que  implemente en mi ejercicio 9.

'''

