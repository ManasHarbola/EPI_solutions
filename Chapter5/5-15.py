from random import randint
def random_subset(n, k):
    subset = []
    encountered = {}

    for i in range(k):
        r = randint(i, n - 1)
        subset.append(encountered.get(r, r))
        encountered[r] = encountered.get(i, i)
    return subset

    '''
    #Alternate approach:
    encountered = {}

    for i in range(k):
        r = randint(i, n - 1)
        i_val = encountered.get(i, i)
        r_val = encountered.get(r, r)
        encountered[r] = i_val
        encountered[i] = r_val
        
    return [encountered[i] for i in range(k)]
    '''
