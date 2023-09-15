# Archivop para recopilar la informacion obtenida

## Preguntas:

> ### P1
> #### 1.
> 
> #### 2. 
> 
> #### 3.
> 

> ### P2
> #### Calculo:
> Use unos cuantos codigos para hacerlo, de los cuales se destacan:
> ```python
>    # Obtiene el valor de pi
>    def p(lista):
>        N = len(lista)
>        p = []
>        for i in range(N):
>            p += [(lista[i]/sum(lista))*100]
>        return p
>    
>    # Obtiene el valor de qi
>    def q(mat_rango, mat_val, rango, val):
>        monto_acumulado = np.dot(mat_rango, mat_val)
>        q = []
>        for i in range(len(rango)):
>            q += [(((val[i])*(rango[i]))/monto_acumulado)*100]
>        return q
>    
>    # Obtiene los valores pero acumulando
>    def acumulador(lista):
>        listaaaa = []
>        for i in range(len(lista)+1):
>            listaaaa += [sum(lista[0:(i)])]
>        return listaaaa
>    
>    # Calcula el coeficiente de gini asociado a los valores p y q
>    def gini(p, q):
>        if not len(p) == len(q):
>            print("Gil ")
>        else:
>            p_q = []
>            for i in range(len(p)):
>                p_q += [abs(p[i]-q[i])]
>            I = (sum(p_q))/(sum(p))
>            return I
> ```
>
> #### Resultados:
> Los resultados estarian dados por la siguiente tabla:
>
>| Institucion              | Coeficiente de Gini | Promedio (?) |
>|--------------------------|---------------------|--------------|
>| Liceo Augusto D'halmar   | 0.048               |              |
>| Colegio Francisco Encina | 0.052               |              |
>| Colegio Suizo            | 0.044               |              |
>| Colegio Akros            | 0.038               |              |
>| Saint Gaspar College     | 0.069               |              |
>| Colegio Calasanz         | 0.058               |              |
> Con promedio no sabia a que se referia, asi que lo deje en blanco. El coeficiente se obtuvo calculando mediante un codigo en python (si, soy medio especialito).