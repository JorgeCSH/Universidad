# Funcion
def CamelCase(s):
    """Retorna un string conteniendo la versión Camel Case del string s español"""
    # escriba aquí su algoritmo
    sa = ""
    n = len(s)
    for i in range(n):
        if s[i] != " ":
            sa += s[i]
        elif i < n - 1 and s[i + 1] != " ":
            sa += s[i]
    if sa[0] == " ":
        sa = sa[1:]
    j = 0
    while j < len(sa):
        if sa[j] == " ":
            sa = sa[:j] + sa[j+1].upper() + sa[j + 2:]
        j += 1
    return sa


# Probar
print(CamelCase("Algoritmos y    estructuras de   datos   "))
gorgor = "    Algoritmos y    estructuras de   datos   "
#print(gorgor)
gorgorr = " Algoritmos y estructuras de datos"
#print(gorgorr)
gorgorgor = "Algoritmos y estructuras de datos"
print(gorgorgor)
print("AlgoritmosYEstructurasDeDatos")






