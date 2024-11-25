import random
import time
import math
from matplotlib import pyplot as plt
from brute_force import threesum
# sizes is size of list and lista is time it took to
# execute threesum function on that list.
sizes = []
lista = []
plot = []
test = []
repeat = 4
# We start at 100 and continue up to 700 with step size 50.abs
for y in range(100, 450, 50):
    # For every list size we append to size list.
    sizes.append(y)
    # How many runs.
    for i in range(repeat):
        lst = random.sample(range(-10**5, 10**5), y)
        start_time = time.time()
        # Performing threesum on list.
        threesum(lst)
        lista.append(time.time() - start_time)
    plot.append(sum(lista)/repeat)
    # plt.scatter(y, (sum(lista)/repeat), c='blue')
# Making each list length appear repeat times
test = sizes
sizes = [item for item in sizes for i in range(repeat)]
# Making values log-scale.
test = [math.log(x) for x in test]
logX = [math.log(x) for x in sizes]
logY = [math.log(y) for y in lista]
x = logX
lista = logY
# Using the same notation that was found in Lecture2.
sxx = 0
sy = 0
sx = 0
sxy = 0
# We follow the formulas in Lecture2 on slide 26.
for i in range(len(x)):
    sxx += (x[i])**2
    sy += lista[i]
    sx += x[i]
    sxy += x[i]*lista[i]
# m is interception and k is slope.
m = (sxx*sy-sx*sxy)/((len(x)*sxx)-sx*sx)
k = (len(x)*sxy - sx*sy)/(len(x)*sxx - sx*sx)
print(f'k = {k}')
print(type(k))
print(type(x))
liney = []
""" for i in range(len(x)):
    liney.append(k*x[i] + m)
for i in range(len(test)):
    plt.scatter(test[i], plot[i], c='blue') """
plt.plot(x, liney, c='red')
# plt.xlim(0, 50)
plt.yscale('log')
plt.xscale('log')
plt.show()
""" liney = [m + k*x for x in logX]
plt.plot(sizes, times, color='green')
plt.plot(logX, liney)

plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show() """
