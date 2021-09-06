"""
Problem Statement:

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]

Output: [18,6,6,6,1,-1]

Constraints:

1 <= arr.length <= 10^4

1 <= arr[i] <= 10^5


Level: Easy

"""
arr = [17,18,5,4,6,1]
def Approch1(arr):#O(n) , sc = O(1)
    n = len(arr)
    max_ele_seen_so_far = arr[n-1]#last ele
    arr[n-1] = -1
    for i in range(n-2,-1,-1):
        temp = arr[i]
        arr[i] = max_ele_seen_so_far
        if temp > max_ele_seen_so_far:
            max_ele_seen_so_far = temp 
    return arr 
         

     
            



print(Approch1(arr))