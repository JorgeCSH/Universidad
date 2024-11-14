# Archivo para realizar la tarea 6 de algoritmos
'''
Increiblemente, Enunciado.

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
############################################################################################################

""" Clase Nodo2.
Representa a los nodos binarios presentes en el arbol.
"""
class Nodo2:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der

    def insert(self,x):
        #return None # Aquí hay que retornar el resultado de insertar x a partir de este punto
        # Caso donde debemos insertar en el hijo izquierdo
        if x<self.info:
            # Caso donde no se produce split en el hijo entregamos puntero al nodo resultante
            if not isinstance(self.izq.insert(x), Nodo3):
                self.izq = self.izq.insert(x)
                return self.izq 
            # Caso donde se produce split en el hijo
            else:
                izq_nuevo, llave, der_nuevo = self.izq.insert(x)
                return (izq_nuevo, llave, Nodo2(der_nuevo, self.info, self.der))

    # Adaptacion de lo realizado en el ejercicio 8 
    def search(self, x):
        # Retornamos None si el siguiente es Nodoe
        if isinstance(self, Nodoe):
            return None
        # Caso donde encontramos el valor
        elif x == self.info:
            return self
        # Caso donde debemos buscar por el arbol izquierdo
        elif x < self.info:
            return self.izq.search(x)
        # Caso donde debemos buscar por el arbol derecho
        elif x > self.info:
            return self.der.search(x)



    def string(self):
        return ("("+self.izq.string()
                +str(self.info)
                +self.der.string()+")")



""" Clase Nodo3.
Clase/estructura que representa los nodos ternarios en el arbol.
"""
class Nodo3:
    def __init__(self, izq, info1, med, info2, der):
        self.izq=izq
        self.info1=info1
        self.med=med
        self.info2=info2
        self.der=der

    def insert(self,x):
        return None # Aquí hay que retornar el resultado de insertar x a partir de este punto



    # Adaptado de lo realizado en el ejercicio 8, analogo al caso de Nodo2 en terminos de cambios.
    def search(self, x):
        # Retornamos None si el siguiente es Nodoe
        if isinstance(self, Nodoe):
            return None
        # Caso donde encontramos alguno de los valores.
        elif x == self.info1 or x == self.info2:
            return self
        # Caso donde debemos buscar por el arbol izquierdo.
        elif x < self.info1:
            return self.izq.search(x)
        # Caso donde debemos buscar por el arbol del medio.
        elif x < self.info2:
            assert x > self.info1       # Assert incluido porsiacaso pero el condicional asegura que no sera mayor.
            return self.med.search(x)
        # Caso donde debemos buscar por el arbol derecho.
        elif x > self.info2:
            return self.der.search(x)


    def string(self):
        return ("("+self.izq.string()
                +str(self.info1)
                +self.med.string()
                +str(self.info2)
                +self.der.string()+")")


""" Clase Nodoe.
Clase que representa a los nodos externos/hojas del arbol. Eta es representada por un cuadradito.
"""
class Nodoe:
    def __init__(self):
        pass

    def insert(self,x):
        return None # Aquí hay que retornar el resultado de insertar x a partir de este punto
    
    # Metodo provisorio... E L I M I N A R def search(self, x):
        return None

    def string(self):
        return"☐"



""" Clase Arbol23
Clase encargada de formar la estructura del arbol 2-3, esta hace uso de las clases Nodo2 y Nodo3.
"""
class Arbol23:
    def __init__(self,raiz=Nodoe()):
        self.raiz=raiz

    def insert(self,x):
        self.raiz=self.raiz.insert(x)   # Esto funciona casi siempre, excepto cuando la antigua raíz se divide
                                        # Usted tiene que poner algo que funcione siempre
    def search(self,x):
        if isinstance(self.raiz, Nodoe):
            return None
        else:
            return self.raiz.search(x)

    def imprimir(self):
        print(self.raiz.string())



"""
Test playground
"""
# Ejemplo original sin el uso del arbol
a=Nodo3(Nodo2(Nodoe(),10,Nodoe()),25,Nodo3(Nodoe(),32,Nodoe(),48,Nodoe()),57,Nodo2(Nodoe(),74,Nodoe()))
#print(a.search(10))
#print(a.search(25))
#print(a.search(57))
#print(a.search(69))

# Ejemplo donde nosotros implementaremos un arbol.
# Formamos el arbol
santa_claus_llego_a_la_ciudad = Arbol23()
# Insertamos los valores
"""
valores_a_insertar = [3, 1, 4, 5, 9, 6, 2]
for i in valores_a_insertar:
    santa_claus_llego_a_la_ciudad.insert(i)
    santa_claus_llego_a_la_ciudad.imprimir()
"""
# Imprimimos el arbol final (ademas de donde imprimiamos cada iteracion
#santa_claus_llego_a_la_ciudad.imprimir()

# Realizamos las busquedas                             
santa_claus_llego_a_la_ciudad.search(2)
santa_claus_llego_a_la_ciudad.search(3)
#santa_claus_llego_a_la_ciudad.search(7)

