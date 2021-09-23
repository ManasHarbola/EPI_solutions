def look_and_say(n):
    def next_number(num_str):
        new_str = ""
        count = 1
        currNum = num_str[0]
        for i in range(1, len(num_str)):
            if num_str[i] != currNum:
                new_str += (str(count) + currNum)
                count = 1
                currNum = num_str[i]
            else:
                count += 1

        new_str += (str(count) + currNum)
        return new_str

    result = "1"
    for i in range(1, n):
        result = next_number(result)
    return result

for i in range(1, 10):
    print(look_and_say(i))
