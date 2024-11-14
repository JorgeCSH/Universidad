

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
                izq_nuevo, llave, der_nuevo = nodo_hijo
                print("2")
                return Nodo3(izq_nuevo, llave, self.izq, self.info, self.der)
            print("1") 
        else:
            # La insertamos recursivamente en el hijo derecho 
            nodo_hijo = self.der.insert(x)
        
            if isinstance(nodo_hijo, tuple):
                izq_nuevo, med, der_nuevo = nodo_hijo
                print("4")
                return Nodo3(self.izq, self.info, izq_nuevo, med, der_nuevo)
            print("3")
        print("mega_return_1")
        return nodo_hijo 

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

    def string(self):
        return ("("+self.izq.string()
                +str(self.info)
                +self.der.string()+")")


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
                izq_nuevo, llave, der_nuevo = nodo_hijo
                print("6")
                banana_split = Nodo2(izq_nuevo, llave, self.med), self.info1, Nodo2(der_nuevo, self.info2, self.der) 
                return banana_split
                #return Nodo3(izq_nuevo, llave, der_nuevo, self.info1, self.llave), self.info2, self.der
            print("5") 
        elif x < self.info2:
            nodo_hijo = self.med.insert(x)

            if isinstance(nodo_hijo, tuple):  # Se produjo una división en el hijo llaveio
                izq_nuevo, llave, der_nuevo = nodo_hijo
                print("8")
                banana_split = Nodo2(self.izq, self.info1, izq_nuevo), llave, Nodo2(der_nuevo, self.info2, self.der) 
                return banana_split 
                #return Nodo3(self.izq, self.info1, izq_nuevo, llave, der_nuevo), self.info2, self.der
            print("7")
        else:
            nodo_hijo = self.der.insert(x)

            if isinstance(nodo_hijo, tuple):  # Se produjo una división en el hijo derecho
                izq_nuevo, llave, der_nuevo = nodo_hijo
                print("10")
                banana_split = Nodo2(self.izq, self.info1, self.med), self.info2, Nodo2(der_nuevo, llave, self.der)
                return banana_split 
                #return Nodo3(self.izq, self.info1, self.llave, self.info2, izq_nuevo), llave, der_nuevo
            print("9")
        print("mega_return_2")
        return nodo_hijo 

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


class Nodoe:
    def __init__(self):
        pass

    def insert(self, x):
        #print("sad")
        return Nodoe(), x, Nodoe()

    def search(self):
        return None
    
    def string(self):
        return"☐"


class Arbol23:
    def __init__(self, raiz=Nodoe()):
        self.raiz = raiz

    def insert(self, x):
        inserta_raiz = self.raiz.insert(x)
        if isinstance(inserta_raiz, tuple):
            izq_nuevo, med, der_nuevo = inserta_raiz
            #print("poto")
            self.raiz = Nodo2(izq_nuevo, med, der_nuevo)
        else:                                               # La raíz se dividió
            #print("ajio")
            self.raiz = inserta_raiz

    def search(self, x):
        return self.raiz.search(x)

    def imprimir(self):
        print(self.raiz.string())
        return self.raiz.string()


# Tests
# Tests originales
# Para probar este código, vamos a construir "a mano" el árbol 2-3 que aparece en el apunte, y luego imprimirlo
a=Nodo3(Nodo2(Nodoe(),10,Nodoe()),25,Nodo3(Nodoe(),32,Nodoe(),48,Nodoe()),57,Nodo2(Nodoe(),74,Nodoe()))
#print(a.string())

# Test solicitados e implementados por yo

gogos = Arbol23()
chococrispis = [3, 1, 4, 5, 9, 6, 2]
#chococrispis = [3]
#chococrispis = [3, 1]
#chococrispis = [3, 1, 4]
#chococrispis = [3, 1, 4, 5]
#chococrispis = [3, 1, 4, 5, 9]
#chococrispis = [3, 1, 4, 5, 9, 6]
#chococrispis = [3, 1, 4, 5, 9, 6, 2]
for i in chococrispis:
    gogos.insert(i)
    gogos.imprimir()
#gogos.imprimir()
#gogos.search(2)
#gogos.search(3)
#gogos.search(7)

#assert gogos.imprimir() == "((☐1☐2☐)3(☐4☐)5(☐6☐9☐))"
#gogos.imprimir()

#assert gogos.imprimir()  == "(((☐2☐3☐)4☐5☐)6☐9☐)"
'''
print()
terrenator = Arbol23()
terrenator.insert(10)
terrenator.insert(25)
terrenator.insert(32)
terrenator.insert(48)
terrenator.insert(57)
terrenator.insert(74)
#print(a.string())
#terrenator.imprimir()


#((☐10☐)25(☐32☐48☐)57(☐74☐))
'''


