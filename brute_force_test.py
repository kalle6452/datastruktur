import random
import time
start_time = time.time()
lst = [-1,0,1,2,-1,-4]
lst = random.sample(range(-10**5, 10**5), 100)
print(lst)
def threesum_brute(lst):
    # There has to be at least 3 elements in original list.
    if len(lst) < 3:
        print('not enough numbers')
    # Empty list where we will put triplets.
    lista = []
    # We compute all possible combinations with 3 for-loops.
    # i represents the actual element while idi represents its index.abs
    # The same principle also applies for j and k.
    for idi, i in enumerate(lst):
        for idj, j in enumerate(lst):
            for idk, k in enumerate(lst):
                # The sum of 3 elements has to be 0 and we have to make sure 
                # that any of the elements don't share the same index.
                if i+j+k == 0 and idi != idj and idi != idk and idj != idk:
                    # We make it a tuple so that it can become a set.
                    lista.append(tuple(sorted([i, j, k])))
    # Removing duplicates
    return list(set(lista))


print(len(lst))    
print(threesum_brute(lst))
print("--- %s seconds ---" % (time.time() - start_time))
