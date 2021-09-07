"""

Problem Statement:

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3

Output: [5,6,7,1,2,3,4]

Explanation:

rotate 1 steps to the right: [7,1,2,3,4,5,6]

rotate 2 steps to the right: [6,7,1,2,3,4,5]

rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2

Output: [3,99,-1,-100]

Explanation: 

rotate 1 steps to the right: [99,-1,-100,3]

rotate 2 steps to the right: [3,99,-1,-100]
"""
# Aprroch 1  tc = O(n*k) , sc = O(1)
#creating a fuction that rotates once and repeat that func k times
arr=[1,2,3,4,5,6,7]
k = 3
n = len(arr)
def rotateOnce(arr,n):
    temp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp

while k > 0:
    rotateOnce(arr,n)
    k-=1
print(arr)

#Best approch tc=O(n), sc=O(1)

#reverse last k vals
#reverse 1 to k-1 vals
#reverse full array

def reverse(arr,l,h):
    while (l<=h):
        temp = arr[l]
        arr[l] = arr[h]
        arr[h] = temp
        l+=1
        h-=1

def rotateKtimes(arr,n,k):
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-k-1)
    reverse(arr, 0, n-1)
    print(arr)

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7]
    rotateKtimes(arr, len(arr), 3)
