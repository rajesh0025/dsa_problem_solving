""" 
Problem Statement:
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.



Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.



Note: You are not suppose to use the library's sort function for this problem.



Example:





Input: [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]


Follow up:




A rather straight forward solution is a two-pass algorithm using counting sort.

First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?

"""
#Approch1 Using any Comparision soring like merge sort O(nlogn)

#Approch2 using counting or bucket sorting  --O(n) , 2 iterations
# count each and append them respectively

#Approch3 -- O(n) , 1 iteration

def DNF(arr,n):
    l=0
    h=n-1
    c=0

    while(c<=h):
        if (arr[c]==0):
            arr[c],arr[l]=arr[l],arr[c]
            l+=1
            c+=1
        elif (arr[c]==1):
            c+=1
        elif (arr[c]==2):
            arr[c],arr[h] = arr[h],arr[c]
            h-=1
    return arr 

if __name__ == "__main__":
    arr = [1,0,1,2,0,2,1,0,2,1,0,0,1,2]
    arr = DNF(arr,len(arr))
    print(arr)