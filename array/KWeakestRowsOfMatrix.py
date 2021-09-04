"""
Problem Statement:

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

 

Example 1:


Input: mat = 

[[1,1,0,0,0],

 [1,1,1,1,0],

 [1,0,0,0,0],

 [1,1,0,0,0],

 [1,1,1,1,1]], 

k = 3

Output: [2,0,3]

Explanation: 

The number of soldiers for each row is: 

row 0 -> 2 

row 1 -> 4 

row 2 -> 1 

row 3 -> 2 

row 4 -> 5 

Rows ordered from the weakest to the strongest are [2,0,3,1,4]

"""

grid = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],
[1,1,1,1,1]]

count = 0
m = len(grid)
n = len(grid[0])
x=[]
for i in range(m):
    ones = 0
    for j in range(n):
        if grid[i][j] == 1:
            ones+=1
    x.append(ones)
print(x)
count = {}
for i,v in enumerate(x):
    count[i]=v
import operator
x = sorted(count.items(),key=operator.itemgetter(1))
print(x)
y=[]
for i in x:
    if i[1]<=2:
        y.append(i[0])
print(y)
        
#approch 2  tc = O(m(n+logn)) , sc  = O(m) m =rows
k=3
count = [(sum(row),i) for i, row in enumerate(grid)]
print(count)
count.sort()#its sort based on first index
out = [count[i][1] for i in range(k)] 
print(f" Linearsearch {out} ")   

#Approch 3 -- binary search O(m(logmn))  sc is O(m)
def binarysearch(row):
    low = 0
    high = len(row)
    while low < high:
        mid = low +(high-low) // 2 

        if row[mid] == 1:
            low = mid+1
        else:
            high = mid 
    return low


count = [(binarysearch(row),i) for i, row in enumerate(grid)]
count.sort()
out = [count[i][1] for i in range(k)]
print(f" Binarysearch {out}")

# Approch 4
#Priority Queue
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Calculate the strength of each row using binary search.
        # Put the strength/index pairs into a priority queue.
        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)

        # Pull out and return the indexes of the smallest k entries.
        # Don't forget to convert them back to positive numbers!
        indexes = []
        while pq:
            strength, i = heapq.heappop(pq)
            indexes.append(-i)

        # Reverse, as the indexes are around the wrong way.
        indexes = indexes[::-1]

        return indexes
