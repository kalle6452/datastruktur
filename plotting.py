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
x = np.arange(100, 750, 50)
x = np.repeat(x, 3)
for y in range(100, 750, 50):
    for i in range(3):
        start_time = time.time()
        lst = random.sample(range(-10**5, 10**5), y)
        threesum(lst)
        if y == 100:
            (plt.scatter(y, (time.time() - start_time), 
                         c=colors[i], label=colors[i]))
        else:
            plt.scatter(y, (time.time() - start_time), c=colors[i])
# Adding extra state
y = 775
for i in range(3):
    start_time = time.time()
    lst = random.sample(range(-10**5, 10**5), y)
    threesum(lst)
    plt.scatter(y, (time.time() - start_time), c=colors[i])
plt.legend()
plt.show()