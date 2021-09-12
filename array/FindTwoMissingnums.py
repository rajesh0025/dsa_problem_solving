"""
Find two Missing Numbers in a Sequence of Consecutive Numbers
"""
#Brute Force with hashmaps by noting elements which are present in array
#O(n),sc O(m), m = 1tolast 

#Approch2 -- Adiition approch  O(n), sc=O(1)

import math 

def FindTwoMissingNums(a,m):
    sum_total = (m*(m+1)/2)
    missing_ele_sum = sum_total - sum(a)
    if missing_ele_sum%2 != 0 :
        missing_ele_avg = int(math.ceil((missing_ele_sum/2)-1))
    else:
        missing_ele_avg = missing_ele_sum/2

    sum_till_avg = ((missing_ele_avg) * (missing_ele_avg+1)/2)

    sum_till_avg_a = 0
    for i in range(len(a)):
        if a[i] <= missing_ele_avg:
            sum_till_avg_a += a[i]
    
    n1 = int(sum_till_avg - sum_till_avg_a)
    n2 = int(missing_ele_sum-n1)

    print(n1,n2)

a = [1,3,5,6]
m= len(a) + 2 
FindTwoMissingNums(a,m)

#Approch 3  -- XOR  O(n), sc=O(1)
def findMissingConsecutive(arr,n):
    xor=arr[0]
    for i in range(1,n):
        xor^=arr[i]
    for i in range(1,n+3):
        xor^=i
    
    set_no=(xor) & ~(xor-1)

    x=0
    y=0
    for i in range(n):
        if arr[i] & set_no:
            x^=arr[i]
        else:
            y^=arr[i]
    for i in range(1,n+3):
        if i & set_no:
            x^=i
        else:
            y^=i
    return x,y

if __name__=='__main__':
    arr=[1,3,5,6]
    
    x,y=findMissingConsecutive(arr,len(arr))
    
    print(x,y)
    