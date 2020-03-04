def rooks_are_safe(chessboard):
    n = len(chessboard)

    for row in range(n):
        row_count = 0
        for col in range(n):
            row_count += chessboard[row][col]
        if row_count > 1:
            return False

    for col in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += chessboard[row_i][col]
        if col_count>1:
            return False
    return True

chessboard = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,1]]

print(rooks_are_safe(chessboard))
