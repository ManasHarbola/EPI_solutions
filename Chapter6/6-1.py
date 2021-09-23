def int_to_string(n):
    if n == 0:
        return '0'

    isNegative = True if n < 1 else False

    if isNegative:
        n = abs(n)

    result = ""
    while n > 0:
        result = chr((n % 10) + 48) + result
        n //= 10
    if isNegative:
        result = '-' + result
    return result

def string_to_int(s):
    if s == '0':
        return 0
    isNegative = True if s[0] == '-' else False

    start = 0
    if s[0] == '-' or s[0] == '+':
        start = 1

    result = 0
    num_digits = len(s)
    for i in range(start, num_digits):
        result += ord(s[i]) - 48
        if i != num_digits - 1:
            result *= 10
    
    if isNegative:
        result *= -1
    return result

