def replace_and_remove(size, s):
    #calculate new size
    if size == 0:
        return 0

    newSize = size
    write_idx = 0
    idx = 0;

    for i in range(size):
        if s[i] != 'b':
            if s[i] == 'a':
                newSize += 1
            s[write_idx] = s[i]
            idx = write_idx
            write_idx += 1
        else:
            newSize -= 1
    
    write_idx = newSize - 1
    for i in reversed(range(idx + 1)):
        if s[i] != 'a':
            s[write_idx] = s[i]
            write_idx -= 1
        else:
            s[write_idx] = 'd'
            s[write_idx - 1] = 'd'
            write_idx -= 2
    
    return newSize


l = ['a', 'c', 'd', 'b', 'b', 'c', 'a']

print(replace_and_remove(len(l), l))
print(l)
