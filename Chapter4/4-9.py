def isPalindrome(num):
    if num < 0:
        return False

    reversedNum = 0
    nCpy = num
    while nCpy:
        reversedNum = (reversedNum * 10) + (nCpy % 10)
        nCpy //= 10

    return reversedNum == num

print(isPalindrome(423324))
print(isPalindrome(-12))
print(isPalindrome(-1))
print(isPalindrome(1))
