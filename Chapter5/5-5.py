def delete_duplicates(lst):
    num_unique = 1
    swap_idx = 1
    prev = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] != prev:
            prev = lst[i]
            lst[swap_idx] =  lst[i]
            swap_idx += 1
    return swap_idx

l1 = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(delete_duplicates(l1))
print(l1)
