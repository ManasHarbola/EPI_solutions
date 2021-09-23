def is_valid_sudoku(partial_assignment):
    #check 9 3x3 subgrids
    for rOffset in range(0, 7, 3):
        for cOffset in range(0, 7, 3):
            appeared = [False] * 9
            for r in range(3):
                for c in range(3):
                    num = partial_assignment[r + rOffset][c + cOffset]
                    if num > 0:
                        if appeared[num - 1]:
                            return False
                        else:
                            appeared[num - 1] = True
    #check columns
    for c in range(9):
        appeared = [False] * 9
        for r in range(9):
            num = partial_assignment[r][c]
            if num > 0:
                if appeared[num - 1]:
                    return False
                else:
                    appeared[num - 1] = True
    #check rows
    for r in range(9):
        appeared = [False] * 9
        for c in range(9):
            num = partial_assignment[r][c]
            if num > 0:
                if appeared[num - 1]:
                    return False
                else:
                    appeared[num - 1] = True
    
    return True

