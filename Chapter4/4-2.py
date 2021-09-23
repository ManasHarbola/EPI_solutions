def swapBits(num, i, j):
    if num & (1 << i) != num & (1 << j):
        num = num ^ (1 << i) ^ (1 << j)
    return num

print(swapBits(73, 1, 6))
