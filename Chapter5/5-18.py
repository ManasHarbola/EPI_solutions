def matrix_in_spiral_order(square_matrix):
    #create result list of precalculated size
    result = [0] * (len(square_matrix) ** 2)
    write_idx = 0
    def spiral_layer(r, c, n):
        nonlocal write_idx
        #base cases
        if n == 1:
            result[write_idx] = square_matrix[r][c]
            return
        #add top row
        for i in range(c, c + n):
            result[write_idx] = square_matrix[r][i]
            write_idx += 1
        #add right column
        for i in range(r + 1, r + n):
            result[write_idx] = square_matrix[i][c + n - 1]
            write_idx += 1
        #add bottom row
        for i in reversed(range(c, c + n - 1)):
            result[write_idx] = square_matrix[r + n - 1][i]
            write_idx += 1
        #add left column
        for i in reversed(range(r + 1, r + n - 1)):
            result[write_idx] = square_matrix[i][c]
            write_idx += 1
        
        return
    
    size = len(square_matrix)
    row = 0
    col = 0
    while size > 0:
        spiral_layer(row, col, size)
        row += 1
        col += 1
        size -= 2

    return result

