def closestInt(num):
    for i in range(63):
        if (num >> i) & 1 != (num >> (i + 1)) & 1:
            num ^= (1 << i) ^ (1 << (i + 1))
            return num
