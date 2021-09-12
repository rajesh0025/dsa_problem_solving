"""

Problem Statement:

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15] 

Output: 5 

Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order. 
Note:




Then length of the input array is in range [1, 10,000].

The input array may contain duplicates, so ascending order here means <=.


Level: Easy
"""
# Approch1 --- O(n^2), O(1)

def FindUnsortedSubarray(nums):
    start =len(nums)
    end = 0
    for i in range(len(nums)-1):#we need to comapre with last ele too so len-1
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                start = min(start,i)
                end = max(end, j)
    if end-start >=0:#Corner case if array already sorted then it returns end = 0 and start = len(nums)
        return end-start + 1
    else:
        return 0

nums = [2,6,4,8,10,9,15]
print(FindUnsortedSubarray(nums))

# Approch 2 --- O(nlogn),O(n)
def FindUnsortedSubarray2(nums):
    start =len(nums)
    end = 0
    sortednums = nums[:]
    sortednums.sort()
    for i in range(len(nums)):
        if sortednums[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)
    if end-start >= 0:
        return end-start + 1
    else:
        return 0

nums = [2,6,4,8,10,9,15]
print(FindUnsortedSubarray2(nums))

#Approch3 --- O(n), O(n)  2 traversals
#Using Stack DS
def FindUnsortedSubarray3(nums):
    stack = []
    start = len(nums)
    end = 0
    #Traverse the array from left to right
    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:
            start = min(start, stack.pop())  # min(7,1) as 6>4
        stack.append(i)

    #Traverse from right to left to get end val
    stack = []
    for i in range(len(nums)-1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            end = max(end, stack.pop())
        stack.append(i)

    if end-start >= 0:
        return end-start + 1
    else:
        return 0

nums = [2,6,4,8,10,9,15]
print(FindUnsortedSubarray3(nums))
