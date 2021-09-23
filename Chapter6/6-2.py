def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == '0':
        return num_as_string

    base_symbols = ('0', '1', '2', '3', '4',
                    '5', '6', '7', '8', '9',
                    'A', 'B', 'C', 'D', 'E',
                    'F')

    isNegative = True if num_as_string[0] == '-' else False
    #slice off sign symbol if necessary
    if num_as_string[0] == '-' or num_as_string[0] == '+':
        num_as_string = num_as_string[1:]

    #convert to base 10 int
    num_base_10 = 0
    base = 1

    for digit in reversed(num_as_string):
        if ord(digit) < 65:
            num_base_10 += (ord(digit) - 48) * base
        else:
            num_base_10 += (ord(digit) - 55) * base

        base *= b1
        
    #convert to new base, in string form
    result = ""
    while num_base_10 > 0:
        result = base_symbols[num_base_10 % b2] + result
        num_base_10 //= b2

    if isNegative:
        result = '-' + result

    return result


print(convert_base(input(), int(input()), int(input())))
