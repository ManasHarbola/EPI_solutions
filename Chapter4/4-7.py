#returns x to the power y
def power(x, y):
    result = 1.0
    if y < 0:
        x = 1 / x
        y *= -1
    while y:
        if y & 1:
            result *= x

        x, y = x * x, y >> 1
    return result

print(power(2, -3))
print(power(2, 15))
