def threesum_brute(lst):
    # There has to be at least 3 elements in original list.
    if len(lst) < 3:
        print('not enough numbers')
    # Empty list where we will put triplets.
    lista = []
    n = len(lst)
    # We compute all possible combinations with 3 for-loops.
    # We use slicing so that redundant operations aren't executed.
    for i in lst[:n-2]:
        print(i)
        for j in lst[i+1:n-1]:
            for k in lst[j+1:n]:
                if i+j+k == 0 and i != j and i != k:
                    # We make it a tuple so that it can become a set.
                    lista.append(tuple(sorted([i, j, k])))
    # Removing duplicates
    return list(set(lista))

    
print(threesum_brute([-1, 0, 1, 2, -1, 4]))
