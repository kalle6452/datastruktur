def selection(lista):
    n = len(lista)
    # No need to iterate over last element.
    for i in range(n-1):
        for j in range(i+1, n):
            lst = lista[i+1:n]
            if lista[j] == min(lst):
                min_idx = j
        lista.insert(i, lista.pop(min_idx))
    return lista


lista = [64, 34, 25, 5, 22, 11, 90, 12]
print(selection(lista))
