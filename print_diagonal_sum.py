def diagonal_sum(myList):
    total = 0
    for i in range(len(myList)):
        print(i)
        print("myList[",i,"][",i,"]")
        total += myList[i][i]
    return total

print(diagonal_sum([[1,0],[1,3]]))
