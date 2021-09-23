def plus_one(numList):
    numList[-1] += 1
    for i in reversed(range(1, len(numList))):
        if numList[i] != 10:
            break
        numList[i] = 0
        numList[i - 1] += 1

    if numList[0] == 10:
        numList[0] = 0
        numList.insert(0, 1)
    return numList

print(plus_one([1, 3, 9]))
print(plus_one([9, 9, 9]))
print(plus_one([1, 8]))
