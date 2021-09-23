def roman_to_integer(s):
    val_map = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    i = 0
    number = 0
    while i < len(s):
        if (i + 1 < len(s)) and (s[i] in {'I', 'X', 'C'}) and (val_map[s[i]] < val_map[s[i + 1]]):
            number += (-val_map[s[i]] + val_map[s[i + 1]])
            i += 2
        else:
            number += val_map[s[i]]
            i += 1

    return number

print(roman_to_integer(input()))
