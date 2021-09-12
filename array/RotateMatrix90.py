"""

Problem Statement:
You are given an n x n 2D matrix representing an image.



Rotate the image by 90 degrees (clockwise).



Note:



You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:





Given input matrix = 

[

  [1,2,3],

  [4,5,6],

  [7,8,9]

],



rotate the input matrix in-place such that it becomes:

[

  [7,4,1],

  [8,5,2],

  [9,6,3]

]

"""

box=[["a","b"],["c","d"],["e","f"]]


#Matrix transpose
rows = len(box)
cols = len(box[0])

box2 = [[""] * rows for _ in range(cols)]

for x in range(rows):
    for y in range(cols):
        box2[y][rows - x - 1] = box[x][y]
print(box2)