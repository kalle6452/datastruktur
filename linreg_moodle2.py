import random
import time
import numpy as np
import math
from matplotlib import pyplot as plt
from brute_force import threesum
sizes = [] # Save list sizes
times = [] # Save average times
repeat = 5 # Times we repeat experiment
for sz in range(100, 300, 50):
    sizes += [sz] # Save size
    total = 0
    for run in range(repeat):
        lst = random.sample(range(1, 300), sz)
        before = time.time()
        sorted = threesum(lst)
        total += time.time() - before
    mean_time = total/repeat # Average time
    print(mean_time)
    times += [mean_time] # Save time
logX = [math.log(x) for x in sizes]
logY = [math.log(y) for y in times]
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
print(f'k = {k}')
 
liney = [m + k*x for x in logX]
plt.plot(sizes, times, color='green')
plt.plot(logX, liney)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show()