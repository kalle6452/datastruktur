import random
import time
start_time = time.time()
# lst = [0, 0, 0]
lst = [-1,0,1,2,-1,-4]
# lst = [0,0,0]
# lst = random.sample(range(1, 10**15), 1000)


def threesum_brute(lst):
    # There has to be at least 3 elements in original list.
    if len(lst) < 3:
        print('not enough numbers')
    # Empty list where we will put triplets.
    lista = []
    n = len(lst)
    # We compute all possible combinations with 3 for-loops.
    # We use slicing so that redundant operations aren't executed.
    for idi, i in enumerate(lst):
        for idj, j in enumerate(lst):
            for idk, k in enumerate(lst):
                # if i+j+k == 0 and lst.index(i) != lst.index(j) and lst.index(i) != lst.index(k):
                if i+j+k == 0 and idi != idj and idi != idk and idj != idk:
                    lista.append(tuple(sorted([i, j, k])))
                    # We make it a tuple so that it can become a set.
                    # lista.append(tuple(sorted([lst.index(i), lst.index(j), lst.index(k)])))
                    #lista.append(tuple(sorted([lst[lst.index(i)], lst[lst.index(j)], lst[lst.index(k)]])))
    # Removing duplicates
    return list(set(lista))


print(len(lst))    
print(threesum_brute(lst))
print("--- %s seconds ---" % (time.time() - start_time))
