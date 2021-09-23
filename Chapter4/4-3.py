def reverseBits(num):
    result = 0
    while num != 0:
        result <<= 1
        result |= (num & 1)
        num >>= 1
    return result

print(reverseBits(0b1110000000000001))
