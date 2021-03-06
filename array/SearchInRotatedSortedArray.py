"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0

Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3

Output: -1
"""

#we need to find any two nums in which their sum is equal to target
#for unsorted array O(n^2)
#for sorted array O(n)
def sortedA(arr,s):
    l=0
    h=len(arr)-1
    while (l!=h):
        if arr[l] + arr[h] == s:
            return True
        if s > arr[l]+arr[h]:
            h-=1
        if s < arr[l]+arr[h]:
            l+=1
       
    return False

#for rotated sorted array
#Approch 2 best 
def pairInSorted(arr,s,n):
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            break
    l=(i+1)%n
    r=i
    
    while(l!=r):
        if(arr[l]+arr[r]==s):
            return True
        
        elif(arr[l]+arr[r]>s):
            r=(n+r-1)%n
        else:
            l=(l+1)%n
        
    return False
        
if __name__=='__main__':
    arr=[11, 15, 26, 38, 9, 10]
    s=19
    print(sortedA(arr,s))
    print(pairInSorted(arr,s,len(arr)))
