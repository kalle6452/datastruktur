import random
import time
import numpy as np
from matplotlib import pyplot as plt


def threesum(lst):
    # Defining variables
    n = len(lst)
    lista = []
    # Can't have triplets if less than three elements.
    if n < 3:
        return []
    # We use 3 for-loops to test all combinations
    # We put limits on range so that we don't perform
    # redundant operations.
    for i in range(n-2):
        x = lst[i]
        for j in range(i+1, n-1):
            y = lst[j]
            for k in range(j+1, n):
                z = lst[k]
                if x + y + z == 0:
                    # We have to put it in tuple
                    # so that we can put it into a set.
                    lista.append(tuple(sorted([x, y, z])))
    # The set removes redundant triplets.
    return list(set(lista))


colors = ['green', 'blue', 'red']
# for i in range(3):
lista = []
x = np.arange(100, 700, 50)
x = np.repeat(x, 5)
for y in range(100, 700, 50):
    for i in range(5):
        start_time = time.time()
        lst = random.sample(range(-10**5, 10**5), y)
        threesum(lst)
        lista.append(time.time() - start_time)
    plt.scatter(y, (sum(lista)/5), c='blue')
    lista = []
y = 775
for i in range(5):
    start_time = time.time()
    lst = random.sample(range(-10**5, 10**5), y)
    threesum(lst)
    lista.append(time.time() - start_time)
plt.scatter(y, (sum(lista)/5), c='blue')
plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show()