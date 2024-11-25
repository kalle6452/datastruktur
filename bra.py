# plots log
import time
import random
import math
from sort_algorithms import (selection, bubble,
                             insertion)
from matplotlib import pyplot as plt
colors = ['green', 'blue', 'red']
sel = []
bub = []
ins = []
sizes = []
repeat = 3
for y in range(100, 4000, 100):
    sizes.append(y)
    lst = random.sample(range(-10**5, 10**5), y)
    for i in range(repeat):
        if i == 0:
            start_time = time.time()
            selection(lst)
            if y == 100:
                (plt.scatter(math.log(y), math.log(time.time() - start_time),
                             c='green', label='selection'))
                sel.append(time.time() - start_time)
            else:
                (plt.scatter(math.log(y), math.log(time.time() - start_time),
                             c='green'))
                sel.append(time.time() - start_time)
        if i == 1:
            start_time = time.time()
            bubble(lst)
            if y == 100:
                (plt.scatter(math.log(y), math.log(time.time() - start_time),
                             c='red', label='bubble'))
                bub.append(time.time() - start_time)
            else:
                (plt.scatter(math.log(y), math.log(time.time() - start_time),
                             c='red'))
                bub.append(time.time() - start_time)
        if i == 2:
            start_time = time.time()
            insertion(lst)
            if y == 100:
                (plt.scatter(math.log(y), math.log(time.time() - start_time),
                             c='blue', label='insertion'))
                ins.append(time.time() - start_time)
            else:
                (plt.scatter(math.log(y), math.log(time.time() - start_time),
                             c='blue'))
                ins.append(time.time() - start_time)
logX = [math.log(x) for x in sizes]
logY = [math.log(y) for y in ins]
x = logX
lista = logY
sxx = 0
sy = 0
sx = 0
sxy = 0
for i in range(len(x)):
    sxx += (x[i])**2
    sy += lista[i]
    sx += x[i]
    sxy += x[i]*lista[i]
m = (sxx*sy-sx*sxy)/((len(x)*sxx)-sx*sx)
k = (len(x)*sxy - sx*sy)/(len(x)*sxx - sx*sx)


plt.xlabel('List size')
plt.ylabel('Run time')
plt.title(f'k = {k}')
plt.legend()
plt.show()
print(k)
