"""

Problem Statement:

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Example 1:


Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

Output: 8

Explanation: There are 8 negatives number in the matrix.
"""
#tc = O(m*n) , sc = O(1)
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count = 0
m = len(grid)
n = len(grid[0])

for i in range(m):
    for j in range(n):
        print(grid[i][j])
        if grid[i][j] <0:
            count+=1
print(count)

# Approch2 O(n+m) , sc O(1)
rows = len(grid)
cols = len(grid[0])
count = 0 
i, j = rows-1, 0
while i >= 0  and j < cols:
    if grid[i][j] <0:
        count += (cols - j)
        i -=1
    else:
        j +=1
print(count)

