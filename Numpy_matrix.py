# Create multidimensional matrix using class
# Use numpy to do basic math.

import numpy as np
import random

class Matrix():
    """Matrix Multiplication"""

    def __init__(self,row,col):

        self.row = row
        self.col = col
        self.mat = []
        for i in range(0,row):
            self.mat.append([])

        for i in range(0,row):
            for j in range(0,col):
                self.mat[i].append(j)
                self.mat[i][j] = 0

        for i in range(0,row):
            for j in range(0,col):
                self.mat[i][j] = random.randint(1,10)
        print self.mat

    def __repr__(self):
        return self.mat

    def __str__(self):
        return self.mat


def Numpy_multiply(arr1,arr2):
    print "numpy addition"
    return arr1+arr2 , arr1*arr2,arr1-arr2



mat1 = Matrix(2,2)
mat2 = Matrix(2,2)


array1 = np.array(mat1.mat)
array2 = np.array(mat2.mat)

print Numpy_multiply(array1,array2)
