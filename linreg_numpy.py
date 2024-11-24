import random
import time
import numpy as np
from matplotlib import pyplot as plt
from brute_force import threesum


colors = ['green', 'blue', 'red']
# for i in range(3):
lista = []
x = np.arange(100, 400, 50)
x = np.repeat(x, 2)
for y in range(100, 400, 50):
    for i in range(2):
        start_time = time.time()
        lst = random.sample(range(-10**5, 10**5), y)
        threesum(lst)
        lista.append(time.time() - start_time)
    plt.scatter(y, (sum(lista)/2), c='blue')
k, m = np.polyfit(x, lista, 1)
print(k)
print(m)
print(x, len(x))
print(lista, len(lista))
# coef = np.polyfit(x, lista, 1)
# poly1d_fn = np.poly1d(coef)
# plt.plot(x, poly1d_fn)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show()
