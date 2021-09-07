"""

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]

Output: 1

Example 2:

Input: [4,1,2,1,2]

Output: 4
"""
#Approch 1 . Brute force O(n^2) , O(1)
arr = [4,1,2,1,2]
for i in range(len(arr)):
    count =0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count+=1
    if count %2 != 0:
        print(arr[i])

# Approch 2 Hashmaps -- tc = O(n) , sc = O(n)

#Approch3  " XOR " -- O(n), scO(1) ---Best Approch 
arr = [4,1,2,1,2]
ans=0
for i in range(len(arr)):
    ans ^=arr[i]
print(ans)

