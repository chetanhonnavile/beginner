import random
class Matrix():

    def __init__(self,row,col):

        self.row = row
        self.col = col

        mat = []
        # first create empty lists of n col
        for i in range(0,col):
            mat.append([])

        #initialise the values with zeroes
        for i in range(0,row):
            for j in range(0,col):
                mat[i].append(j)
                mat[i][j] = 0

        for i in range(0,row):
            for j in range(0,col):
                mat[i][j] = random.randint(1,100)

        print mat

Matr = Matrix(2,20)
