# Corresponde al archivo en python para hacer el ejercicio 6.2 del apunte.
''' Enunciado (para no tabulear a cada rato)
En este ejercicio usted debe modificar la implementación dada para asegurar que cada nodo del árbol se visite solo una vez, asegurando de esta manera que el 
costo de determinar si un árbol es AVL sea Theta(n)$.

Para esto, usted debe fusionar las funciones ``altura`` y ``es_AVL``en una sola función ``altura_AVL``, que retorne una tupla $(h,a)$, donde $h$ es la altura
y $a$ es un booleano que dice si el árbol es AVL. De esta manera, al invocar la función se tiene de una sola vez toda la información necesaria.
'''
# Clases 
class Nodoi:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der

    def altura(self):
        return 1+max(self.izq.altura(),self.der.altura())

    def es_AVL(self):
        return abs(self.izq.altura()-self.der.altura())<=1 \
                and self.izq.es_AVL() and self.der.es_AVL()

    def __str__(self):
        return "("+self.izq.__str__()+str(self.info)+self.der.__str__()+")"

class Nodoe:
    def __init__(self):
        pass

    def altura(self):
        return 0

    def es_AVL(self):
        return True

    def __str__(self):
        return"☐"

class Arbol:
    def __init__(self,raiz=Nodoe()):
        self.raiz=raiz

    def es_AVL(self):
        return self.raiz.es_AVL()

    def __str__(self):
        return self.raiz.__str__()


# Probar
# Prueba 1
a1=Arbol(Nodoi(Nodoi(Nodoe(),1,Nodoe()),
            2,
            Nodoi(Nodoe(),3,Nodoi(Nodoe(),4,Nodoe()))))
print(a1)
print(a1.es_AVL())

# Prueba 2
a1=Arbol(Nodoi(Nodoi(Nodoe(),1,Nodoe()),
            2,
            Nodoi(Nodoe(),3,Nodoi(Nodoe(),4,Nodoe()))))
print(a1)
print(a1.es_AVL())

