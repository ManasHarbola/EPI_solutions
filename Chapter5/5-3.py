def multiply(num1, num2):
    result = [0] * (len(num1) + len(num2))
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i + j + 1] += num1[j] * num2[i]
    for i in reversed(range(1, len(result))):
        result[i - 1] += (result[i] // 10)
        result[i] %= 10
    for i in range(len(result)):
        if result[i] != 0 or i == len(result) - 1:
            result[i] *= sign
            return result[i:]

print(multiply([5,4,9,1], [7,3,0,2]))
