"""
Problem Statement:

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:





Input: 

[

  [1,1,1],

  [1,0,1],

  [1,1,1]

]

Output: 

[

  [1,0,1],

  [0,0,0],

  [1,0,1]

]

"""

def setZeroes(matrix):# O(M * N)  , sc = o(m+n)
    m = len(matrix)
    n = len(matrix[0])

    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix

matrix = [
    [1,1,1],

  [1,0,1],

  [1,1,1]
]

print(setZeroes(matrix))

m =[

  [0,1,2,0],

  [3,4,5,2],

  [1,3,1,5]

]
print(setZeroes(m))


 #Approch2 
def setZeroes2(matrix):
    row_flag, col_flag = False, False
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if i==0 and matrix[i][j] == 0 :#first row and  first row elemenrs
                row_flag = True
            if j==0 and matrix[i][j] == 0: #first col and first col elemets
                col_flag = True
            if matrix[i][j] == 0:#update first row and col
                matrix[0][j] = 0 
                matrix[i][0] = 0
        
    for i in range(1,m):#except first r and c
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] =0
            
    if row_flag:
        for i in range(n):
            matrix[0][i] = 0
    if col_flag:
        for j in range(m):
            matrix[j][0] = 0
    return matrix

matrix = [

  [1,1,1],

  [1,0,1],

  [1,1,1]

]

print(setZeroes2(matrix))

