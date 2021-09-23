def reverse_words(s):
    if len(s) <= 1:
        return

    s.reverse()
    def reverse(s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

    start = 0
    end = 0
    while end < len(s):
        if s[end] == ' ':
            reverse(s, start, end - 1)
            start, end = end + 1, end + 1
        else:
            end += 1
    
    #check if there was a last word which needed reversal
    if s[end - 1] != ' ':
        reverse(s, start, end - 1)

