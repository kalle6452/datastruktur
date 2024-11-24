import time
import random


def selection(lista):
    n = len(lista)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista.insert(i, lista.pop(min_idx))
    return lista


def bubble(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if lista[j+1] < lista[j]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def insertion(lista):
    n = len(lista)
    for i in range(1, n):
        for j in range(n):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def insertion_2(lst):
    n = len(lst)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if (lst[j] > lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_3(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


lista = [64, 34, 25, 5, 22, 11, 90, 12]

lista = random.sample(range(-10**5, 10**5), 4000)
print(insertion_3(lista))
""" start_time = time.time()
insertion(lista)
print(time.time() - start_time)


start_time = time.time()
insertion_2(lista)
print(time.time() - start_time)


start_time = time.time()
insertion_3(lista)
print(time.time() - start_time) """

""" start_time = time.time()
bubble(lista)
print(time.time() - start_time)

start_time = time.time()
insertion(lista)
print(time.time() - start_time)  """