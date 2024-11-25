import time
import random
import math
from sort_algorithms import (selection, bubble, insertion_2,
                             insertion_3, insertion)
from matplotlib import pyplot as plt
colors = ['green', 'blue', 'red']
sel = []
bub = []
ins = []
sizes = []
repeat = 3
for y in range(100, 2000, 100):
    sizes.append(y)
    lst = random.sample(range(-10**5, 10**5), y)
    for i in range(repeat):
        if i == 0:
            start_time = time.time()
            selection(lst)
            if y == 100:
                (plt.scatter(y, (time.time() - start_time),
                             c='green', label='selection'))
                sel.append(time.time() - start_time)
            else:
                (plt.scatter(y, (time.time() - start_time),
                             c='green'))
                sel.append(time.time() - start_time)
        if i == 1:
            start_time = time.time()
            bubble(lst)
            if y == 100:
                (plt.scatter(y, (time.time() - start_time),
                             c='red', label='bubble'))
                bub.append(time.time() - start_time)
            else:
                (plt.scatter(y, (time.time() - start_time),
                             c='red'))
                bub.append(time.time() - start_time)
        if i == 2:
            start_time = time.time()
            insertion(lst)
            if y == 100:
                (plt.scatter(y, (time.time() - start_time),
                             c='blue', label='insertion'))
                ins.append(time.time() - start_time)
            else:
                (plt.scatter(y, (time.time() - start_time),
                             c='blue'))
                ins.append(time.time() - start_time)

# sizes = [item for item in sizes for i in range(repeat)]
logX = [math.log(x) for x in sizes]
logY = [math.log(y) for y in bub]
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
print(k)
