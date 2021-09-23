def is_palindrome(s):
    sz = len(s)
    if sz == 0 or sz == 1:
        return True
    
    i, j = 0, sz - 1

    while i < j:
        leftChr, rightChr = s[i].upper(), s[j].upper()
        #check to see if either character is not alphanumeric
        if ord(leftChr) < 65 or ord(leftChr) > 90:
            i += 1
            continue
        if ord(rightChr) < 65 or ord(leftChr) > 90:
            j -= 1
            continue
        
        #at this point, both characters must be alphanumeric
        if leftChr != rightChr:
            return False
        else:
            i += 1
            j -= 1


    return True
