def particionHoare(a,p):
    # retorna el punto de corte, el número de elementos <p y la lista particionada
    n=len(a)
    (i,j)=(0,n-1) #inicialmente todos los elementos son desconocidos
    while i<=j: # aún quedan elementos desconocidos
        if a[i]<p:
            i+=1
        elif a[j]>p:
            j-=1
        else:
            (a[i],a[j])=(a[j],a[i]) # intercambio
            i+=1
            j-=1
    return (p,i,a)

def verifica_particion(t): # imprime y chequea partición
    (p,m,a)=t
    # p=punto de corte, m=número de elementos <p, a=lista completa particionada
    print(a[0:m],p,a[m:])
    print("Partición OK" if (m==0 or max(a[0:m])<p) and (m==len(a) or min(a[m:])>p)
          else "Error")


verifica_particion(particionHoare([73,21,34,98,56,37,77,65,82,15,36],50))
verifica_particion(particionHoare([73,21,34,98,56,37,77,65,82,15,36],0))
verifica_particion(particionHoare([73,21,34,98,56,37,77,65,82,15,36],100))


# Contrario a la version de Hoare, el indice j
def particionLomuto(a, p):
    # retorna el punto de corte, el número de elementos <p y la lista particionada
    n = len(a)                                           # Jorge: largo de la lista, sera recorrido en su totalidad por "j"
    (i, j) = (0,0)                                       # Jorge: tupla de indices, en este caso las dos aumentan, por ende se parte en cero (inicio)
    # escribir acá el algoritmo de partición de Lomuto
    while j<n:                                           # Jorge: tenemos que el "j" siempre incrementa, por eso usamos un while
        if a[j]<p:                                       # Jorge: siguiendo la indicacion, en caso de que sea menor, intercambiamos y aumentamos el indice "i"
            (a[i], a[j]) = (a[j], a[i])                  # Jorge: intercambio
            i+=1                                         # Jorge: se cumple la condicion => aumenta "i"
        j+=1                                             # Jorge: aumenta "j" durante toda la ejecucion
    return (p, i, a)                                     # Jorge: tupla de resultado, p = corte, i= indice de corte, a = lista original

verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],50))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],0))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],100))
