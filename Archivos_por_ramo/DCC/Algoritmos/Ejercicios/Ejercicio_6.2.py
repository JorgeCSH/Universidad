# Corresponde al archivo en python para hacer el ejercicio 6.2 del apunte.
''' Enunciado (para no tabulear a cada rato)
En este ejercicio usted debe modificar la implementación dada para asegurar que cada nodo del árbol se visite solo una vez, asegurando de esta manera que el 
costo de determinar si un árbol es AVL sea Theta(n)$.

Para esto, usted debe fusionar las funciones ``altura`` y ``es_AVL``en una sola función ``altura_AVL``, que retorne una tupla $(h,a)$, donde $h$ es la altura
y $a$ es un booleano que dice si el árbol es AVL. De esta manera, al invocar la función se tiene de una sola vez toda la información necesaria.
'''
# Clases 

''' Clase Nodoi

No se retiraron los metodos originales, sin embargo lo que si se hizo fue implementar el nuevo metodo, metodo
que estuvo basado en el funcionamiento de los metodos originales, solo que en vez se obtienen los datos de una
tupla que contiene los datos que originalmnete eran accedidos uno a uno, esto en la clase del nodo externo que 
sigue a esta.
'''
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

    '''
    Metodo solicitado, realiza las mismas operaciones solo que esta vez los datos los obtiene de una en una tupla,
    de ahi son procesador por separado y retornados en una nueva tupla como solicitado.
    '''
    def altura_AVL(self):
        (h_izq,r_izq) =self.izq.altura_AVL()
        (h_der,r_der) =self.der.altura_AVL()
        h = 1+max(h_izq, h_der)
        a = abs(h_izq - h_der)
        bool_a = a<=1 and r_izq and r_der
        return (h , bool_a)

    def __str__(self):
        return "("+self.izq.__str__()+str(self.info)+self.der.__str__()+")"

''' Clase Nodoe
Se implemento el metodo, lo que realiza es en ciertos terminos lo mismo que los metodos altura y es_AVL
original pero en una tupla, la cual es despues usada por Nodoi
'''
class Nodoe:
    def __init__(self):
        pass

    def altura(self):
        return 0

    def es_AVL(self):
        return True
    '''
    Metodo implementado, tupla con los valores.
    '''
    def altura_AVL(self):
        return (0,True)
    
    def __str__(self):
        return"☐"

class Arbol:
    def __init__(self,raiz=Nodoe()):
        self.raiz=raiz

    def es_AVL_or(self):
        return self.raiz.es_AVL()

    def es_AVL(self):
        return self.raiz.altura_AVL()

    def __str__(self):
        return self.raiz.__str__()


# Probar
# Prueba 1
a1=Arbol(Nodoi(Nodoi(Nodoe(),1,Nodoe()), 2, Nodoi(Nodoe(),3,Nodoi(Nodoe(),4,Nodoe()))))
print(a1)
print(a1.es_AVL())

# Prueba 2
a2=Arbol(Nodoi(Nodoi(Nodoe(),1,Nodoe()),
            2,
            Nodoi(Nodoe(),3,Nodoi(Nodoe(),4,Nodoi(Nodoe(),5,Nodoe())))))
print(a2)
print(a2.es_AVL())
