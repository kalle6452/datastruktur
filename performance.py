import time
import random
from sort_algorithms import (selection, bubble, insertion_2, 
                             insertion_3, insertion)
from matplotlib import pyplot as plt
colors = ['green', 'blue', 'red']
for y in range(100, 1000, 100):
    lst = random.sample(range(-10**5, 10**5), y)
    for i in range(3):
        if i == 0:
            start_time = time.time()
            selection(lst)
            if y == 100:
                (plt.scatter(y, (time.time() - start_time), 
                             c='green', label='selection'))
            else:
                (plt.scatter(y, (time.time() - start_time), 
                             c='green'))
        if i == 1:
            start_time = time.time()
            bubble(lst)
            if y == 100:
                (plt.scatter(y, (time.time() - start_time), 
                             c='red', label='bubble'))
            else:
                (plt.scatter(y, (time.time() - start_time), 
                             c='red'))
        if i == 2:
            start_time = time.time()
            insertion(lst)
            if y == 100:
                (plt.scatter(y, (time.time() - start_time), 
                             c='blue', label='insertion'))
            else:
                (plt.scatter(y, (time.time() - start_time), 
                             c='blue'))


plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show()