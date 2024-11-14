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
        self.izq = izq
        self.info = info
        self.der = der

    def insert(self, x):
        if x < self.info:
            # La insertamos recursivamente en el hijo izquierdo
            nodo_hijo = self.izq.insert(x)
            
            # Caso donde se produce split en el nodo hijo.
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo3(izq_nuevo, key, self.izq, self.info, self.der) 
                return resultado 
            else:
                resultado = Nodo2(nodo_hijo, self.info, self.der)
                return resultado

        else:
            # La insertamos recursivamente en el hijo derecho 
            nodo_hijo = self.der.insert(x)
        
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo3(self.izq, self.info, izq_nuevo, key, der_nuevo)
                return resultado 
            else: 
                resultado = Nodo2(self.izq, self.info, nodo_hijo)
                return resultado

    # Adaptacoion de lo realizado en el ejercicio 8 
    def search(self, x):
        # Caso donde debemos buscar por el arbol izquierdo
        if x < self.info:
            return self.izq.search(x)
        # Caso donde debemos buscar por el arbol derecho
        elif x > self.info:
            return self.der.search(x)
        # Caso donde encontramos el valor
        elif x == self.info:
            return self
        else:
            return None

    def string(self):
        return ("("+self.izq.string()
                +str(self.info)
                +self.der.string()+")")


""" Clase Nodo3.
Clase/estructura que representa los nodos ternarios en el arbol.
"""
class Nodo3:
    def __init__(self, izq, info1, med, info2, der):
        self.izq = izq
        self.info1 = info1
        self.med = med
        self.info2 = info2
        self.der = der

    def insert(self, x):
        if x < self.info1:
            nodo_hijo = self.izq.insert(x)
            if isinstance(nodo_hijo, tuple):  # Se produjo una división en el hijo izquierdo
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo2(izq_nuevo, key, self.med), self.info1, Nodo2(der_nuevo, self.info2, self.der) 
                return resultado
            else:   
                resultado = Nodo3(nodo_hijo, self.info1, self.med, self.info2, self.der)
                return resultado
        elif x < self.info2:
            nodo_hijo = self.med.insert(x)
            if isinstance(nodo_hijo, tuple):  # Se produjo una división en el hijo keyio
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo2(self.izq, self.info1, izq_nuevo), key, Nodo2(der_nuevo, self.info2, self.der) 
                return resultado 
            else:
                resultado = Nodo3(self.izq, self.info1, nodo_hijo, self.info2, self.der)
                return resultado
        else:
            nodo_hijo = self.der.insert(x)
            if isinstance(nodo_hijo, tuple):  # Se produjo una división en el hijo derecho
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo2(self.izq, self.info1, self.med), self.info2, Nodo2(der_nuevo, key, self.der)
                return resultado 
            else:
                resultado = Nodo3(self.izq, self.info1, self.med, self.info2, nodo_hijo)
                return resultado

    # Adaptado de lo realizado en el ejercicio 8, analogo al caso de Nodo2 en terminos de cambios.
    def search(self, x):
        # Caso donde encontramos alguno de los valores.
        if x == self.info1 or x == self.info2:
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
        # Caso nuevo, no encontramos el valor. (CORREGIR)
        else:
            return None

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

    def insert(self, x):
        return Nodoe(), x, Nodoe()

    def search(self, x):
        return None
    
    def string(self):
        return"☐"


""" Clase Arbol23
Clase encargada de formar la estructura del arbol 2-3, esta hace uso de las clases Nodo2 y Nodo3.
"""
class Arbol23:
    def __init__(self, raiz=Nodoe()):
        self.raiz = raiz

    def insert(self, x):
        inserta_raiz = self.raiz.insert(x)
        if isinstance(inserta_raiz, tuple):
            izq_nuevo, med, der_nuevo = inserta_raiz
            self.raiz = Nodo2(izq_nuevo, med, der_nuevo)
            return self.raiz
        else:                                               # La raíz se dividió
            self.raiz = inserta_raiz
            return self.raiz

    def search(self, x):
        return self.raiz.search(x)

    def imprimir(self):
        print(self.raiz.string())

'''
Testeamos el codigo
'''
# Tests originales
print(f"Tests originales")
# Para probar este código, vamos a construir "a mano" el árbol 2-3 que aparece en el apunte, y luego imprimirlo
a=Nodo3(Nodo2(Nodoe(),10,Nodoe()),25,Nodo3(Nodoe(),32,Nodoe(),48,Nodoe()),57,Nodo2(Nodoe(),74,Nodoe()))
print(a.string())
#print(a.search(10))
#print(a.search(25))
#print(a.search(57))
#print(a.search(69))
print(f"\n")


# Test solicitados
print(f"Tests solicitados")
# Formamos el arbol
b = Arbol23()

# Insertamos los valores e imprimimos a medida que insertamos
valores_a_insertar = [3, 1, 4, 5, 9, 6, 2]
for i in valores_a_insertar:
    print(f"insertamos {i}")
    b.insert(i)
    b.imprimir()
    print()
#assert b.imprimir() == "((☐1☐2☐)3(☐4☐)5(☐6☐9☐))" # Originalmente habia agregado un "return" para testear

print(f"Imprimimos resultado final")
b.imprimir()
print(f"\n\nRealizamos las busquedas (search()) solicitados, de no funcionar se caeria el programa")
b.search(2)
print(f"Busqueda de {2}: {b.search(2)}\n")
b.search(3)
print(f"Busqueda de {3}: {b.search(3)}\n")
b.search(7)
print(f"Busqueda de {7}: {b.search(7)}\n")

# Error original que me estaba dando
#"(((☐2☐3☐)4☐5☐)6☐9☐)"
