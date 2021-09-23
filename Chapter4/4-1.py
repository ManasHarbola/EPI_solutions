def getParity(num):
    parity = 0

    while num != 0:
        parity ^= num & 1
        num = num & (num - 1);
    
    return parity

print(getParity(15))
print(getParity(32))
