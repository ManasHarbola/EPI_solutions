def reverseDigits(num):
    result, nCpy = 0, abs(num)
    while nCpy:
        result *= 10
        result += (nCpy % 10)
        nCpy //= 10
    if num < -1:
        result *= -1
    return result

print(reverseDigits(-431))
print(reverseDigits(345))

