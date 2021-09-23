def snake_string(s):
    lst = []
    for i in range(1, len(s), 4):
        lst.append(s[i])
    for i in range(0, len(s), 2):
        lst.append(s[i])
    for i in range(3, len(s), 4):
        lst.append(s[i])

    return ''.join(lst)

print(snake_string("Hello World!"))
