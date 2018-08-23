def minSort(L):
    if L == []:
        return []
    m = min(L)
    return [m] + minSort([x for x in L if x != m])

L = [ 2, 13, 5, 13, 7, 2, 4 ]
print('minSort(', L, ') = ', minSort(L), sep='')


