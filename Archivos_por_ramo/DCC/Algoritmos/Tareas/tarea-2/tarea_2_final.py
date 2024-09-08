import numpy as np

n = 7

i_esimo = np.log2(n + 1)
i_max = int(i_esimo)-
secuencia = []
while i_max > 0:
    d_i = 2 ** i_max - 1
    secuencia += [int(d_i)]
    i_max -= 1

print(secuencia)
for d_i in secuencia:
    print(d_i)





