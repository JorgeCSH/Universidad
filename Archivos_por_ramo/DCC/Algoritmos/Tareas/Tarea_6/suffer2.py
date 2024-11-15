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
            nodo_hijo = self.izq.insert(x)
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo3(izq_nuevo, key, der_nuevo, self.info, self.der)
                return resultado
            else:
                print(type(self))
                resultado = Nodo2(nodo_hijo, self.info, self.der)
                return resultado
        else:
            nodo_hijo = self.der.insert(x)
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo3(self.izq, self.info, izq_nuevo, key, der_nuevo)
                return resultado
            else:
                resultado = Nodo2(self.izq, self.info, nodo_hijo)
                return resultado
    def search(self, x):
        if x == self.info:
            return self
        elif x < self.info:
            if type(self.izq) == Nodoe or type(self.der) == Nodoe:
              return None
            return self.izq.search(x)
        elif x > self.info:
            if type(self.izq) == Nodoe or type(self.der) == Nodoe:
              return None
            return self.der.search(x)

    def string(self):
        return ("("+self.izq.string()
                +str(self.info)
                +self.der.string()+")")

""" Clase Nodo3.
Clase/estructura que representa los nodosternarios en el arbol.
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
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo2(izq_nuevo, key, self.med), self.info1, Nodo2(der_nuevo, self.info2, self.der)
                return resultado
            else:
                resultado = Nodo3(nodo_hijo, self.info1, self.med, self.info2, self.der)
                return resultado
        elif x < self.info2:
            nodo_hijo = self.med.insert(x)
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo2(self.izq, self.info1, izq_nuevo), key, Nodo2(der_nuevo, self.info2, self.der)
                return resultado
            else:
                resultado = Nodo3(self.izq, self.info1, nodo_hijo, self.info2, self.der)
                return resultado
        else:
            nodo_hijo = self.der.insert(x)
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, key, der_nuevo = nodo_hijo
                resultado = Nodo2(self.izq, self.info1, self.med), self.info2, Nodo2(izq_nuevo, key, der_nuevo)
                return resultado
            else:
                resultado = Nodo3(self.izq, self.info1, self.med, self.info2, nodo_hijo)
                return resultado

    def search(self, x):
        if x == self.info1 or x == self.info2:
            return self
        if x < self.info1:
            if type(self.izq) == Nodoe or type(self.med) == Nodoe or type(self.der) ==Nodoe:
                return None
            return self.izq.search(x)
        elif x < self.info2:
            if type(self.izq) == Nodoe or type(self.med) == Nodoe or type(self.der) ==Nodoe:
                return None
            return self.med.search(x)
        elif x > self.info2:
            if type(self.izq) == Nodoe or type(self.med) == Nodoe or type(self.der) ==Nodoe:
                return None
            return self.der.search(x)

    def string(self):
        return ("("+self.izq.string()
                +str(self.info1)
                +self.med.string()
                +str(self.info2)
                +self.der.string()+")")

""" Clase Nodoe.
Clase que representa a los nodos externos/hojas del arbol. Eta es representada
 por un cuadradito.
"""
class Nodoe:
    def __init__(self):
        pass

    def insert(self, x):
        return Nodoe(), x, Nodoe()

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
            izq_nuevo, key, der_nuevo = inserta_raiz
            self.raiz = Nodo2(izq_nuevo, key, der_nuevo)
            return self.raiz
        else:
            self.raiz = inserta_raiz
            return self.raiz

    def search(self, x):
        return self.raiz.search(x)

    def imprimir(self):
        print(self.raiz.string())
''' Primera prueba: arbol original
Aca testearemos montar de manera manual el arbol que originalmente fue creado
a mano en el enunciado y en el apunte para los valores 10, 25, 32, 48, 57, 74.
'''
print(f'Arbol original, "A".\nComo deberia ser: ((☐10☐)25(☐32☐48☐)57(☐74☐)) \n')
# Creamos el arbol "A"
A = Arbol23()

# Lista de valores
lista_arbol_original = [10, 32, 25, 74, 57, 48]

# Insertamos valor por valor
for i in lista_arbol_original:
    #print(f"insertamos {i}")
    A.insert(i)
    #A.imprimir()
    #print()

# Imprimimos el arbol
print(f"Imprimimos resultado final.")
A.imprimir()
print(f'\n')


###############################################################################
print("##############################################################################")
''' Segunda prueba: arbol con secuencia solicitada
Aca testearemos/montaremos el arbol con la secuencia de valores solicitada 
en un inicio, las cuales son: 3, 1, 4, 5, 9, 6, 2, todo en ese orden respectivo.
'''
print(f'Arbol con secuencia solicitada, "B".\nComo deberia ser: ((☐1☐2☐)3(☐4☐)5(☐6☐9☐)) \n')
# Creamos el arbol "B"
B = Arbol23()

# Insertamos los valores e imprimimos a medida que insertamos
valores_a_insertar = [3, 1, 4, 5, 9, 6, 2]
for j in valores_a_insertar:
    #print(f"insertamos {j}")
    B.insert(j)
    #B.imprimir()
    #print()

# Realizamos las pruebas solicitadas.
print(f"Imprimimos resultado final")
B.imprimir()
print(f"\n\nRealizamos las busquedas (search()) solicitados, de no funcionar se caeria el programa.")
# Buscamos el valor "2", simplemente deberia no botar el programa pues si esta
B.search(2)
# Buscamos el valor "3", simplemente deberia no botar el programa pues si esta
B.search(3)
# Buscamos el valor "7", deberia dar None
B.search(7)


###############################################################################
print("##############################################################################")
''' Tercera prueba (extra): insertar el arbol restante del apunte
En esta prueba lo que haremos sera insertar el arbol del apunte donde se 
insertan los valores 1, 2, 3, 4, 5, 6, 7, en ese orden para corroborar 
el correcto funcionamiento.
'''
print(f'Extra: arbol del apunte (al final), "C".\nComo deberia ser: (((☐1☐)2(☐3☐))4((☐5☐)6(☐7☐))) \n')
# Creamos el arbol "C"
C = Arbol23()

# Insertamos los valores
secuencia_lineal = [1, 2, 3, 4, 5, 6, 7]
for k in secuencia_lineal:
    #print(f"insertamos {k}")
    C.insert(k)
    #c.imprimir()
    #print()

# Imprimimos el arbol
print(f"Imprimimos resultado final")
C.imprimir()

