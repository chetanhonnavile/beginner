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

chessboard = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,0]]
print("=======")
print(rooks_are_safe(chessboard))


def rooks_safe(chessboard):
    n = len(chessboard)
    for row in range(n):
        total_row_count = 0
        for item in range(n):
            print(chessboard[row][item]),
            total_row_count += chessboard[row][item]
        if total_row_count > 1:
            return "Rooks are not safe"
        
        print("\n")
    print "======="
    for col in range(n):
        total_col_count = 0
        for item in range(n):
            print(chessboard[item][col]),
            total_col_count += chessboard[item][col]
        if total_col_count > 1:
            return "Rooks are not safe"
        
        print("\n")
    return "rooks are safe"
        

print("------------")
print(rooks_safe(chessboard))
