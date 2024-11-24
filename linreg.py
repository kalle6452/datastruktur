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
x = np.arange(100, 400, 50)
x = np.repeat(x, 2)
for y in range(100, 400, 50):
    for i in range(2):
        start_time = time.time()
        lst = random.sample(range(-10**5, 10**5), y)
        threesum(lst)
        lista.append(time.time() - start_time)
    plt.scatter(y, (sum(lista)/2), c='blue')


def mean(length):
    return sum(length)/(len(length))


def variance(length, mean):
    for i in length:
        var = sum((x-mean)**2)
        return var


def coefficient(x, mean_x, lista, mean_lista, var_x):
    covar = 0
    for i in range(len(x)):
        covar += (x[i] - mean_x)*(lista[i] - mean_lista)
    k = covar/var_x
    return k


def intercept(mean_y, mean_x, k):
    m = mean_y - k*mean_x
    return m


# Putting into use
# Mean
print(lista)
mean_x = mean(x)
mean_y = mean(lista)
# Variance
var_x = variance(x, mean_x)
# Coefficient
k = coefficient(x, mean_x, lista, mean_y, var_x)
# Intercept
m = intercept(mean_y, mean_x, k)
print(k)
print(m)
x = np.arange(0, 100, 400)
y = k*x + m
plt.plot(x, y)
# För regression, x = x, lista = y
# We start by defining functions.
# Mean
plt.yscale('log')
plt.xscale('log')
plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show()


""" mean_lista = sum(lista)/(len(lista))
mean_x = sum(x)/(len(x))
# Variance
var_lista = sum([(lista-mean_lista)**2 for lista in lista])
var_x = sum([(x-mean_x)**2 for x in x])
# Covariance
covar = 0.0
for i in range(len(x)):
    covar += (x[i] - mean_x) * (lista[i] - mean_lista)
print(covar)
# Coefficients, y=kx+m, y=b0+b1*x
k = covar/mean_x
m = mean_lista - k*mean_x
print(k)
print(m) """
# var = sum( (y - mean(y))**2)
""" plt.yscale('log')
plt.xscale('log')
plt.xlabel('List size')
plt.ylabel('Run time')
plt.legend()
plt.show() """