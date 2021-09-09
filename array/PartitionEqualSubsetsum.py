"""
Problem Statement:
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false"""

a =  [1, 5, 11, 5]

sum = 0
for i in range(len(a)):
    sum +=a[i]

l=sum
r=0
for i in range(len(a)-1,-1,-1):
    r+=a[i]
    l-=a[i]
    if r==l:
        print(True)

def getSplitpoint(a, n):
    l = 0
    r = 0
    for i in range(n):
        l+=a[i]
    for i in range(n-1, -1, -1):
        r+=a[i]
        l-=a[i]
        if l==r:
            return True
    return False

if __name__ == "__main__":
    a = [1, 2, 3, 5]
    print(getSplitpoint(a,len(a)))    