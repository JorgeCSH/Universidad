import matplotlib.pyplot as plt
OX = []
for i in range(1, 10):
    OX += [i]
OY = []
for i in range(1, 10):
    OY += [i**1.5]



plt.figure(figsize=(7,5))
plt.plot(OX, OY, label = '', color = 'green')
plt.title("")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.legend()
plt.show()