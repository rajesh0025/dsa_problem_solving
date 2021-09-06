"""
If we do XOR of two same numbers then the value will be zero.
Example:
(1^1)^(2^2)^(3^3)=0
If you XOR the index and the respective value in the array and if there is no missing number then the whole XOR value will be zero.

Array : 1 2 3 5
Index:  1 2 3 4
Initialise the final variable with N.
Apply XOR on final value and each element index with its respective number in the array
From the above example, we get
5^(1^1)^(2^2)^(3^3)^(5^4)
If you rearrange the terms
(1^1)^(2^2)^(3^3)^4^(5^5) then you will be left behind the value 4 
"""
# Approch1
#Addition based approch O(n), sc=O(1) It does havve overflow problem
a=[1,9,3,7,6,5,4,8,2]
n=10
def FMN(a,n):
    sum = (n*(n+1))/2
    print(sum)
    for i in range (n-1):
        sum = sum - a[i]
    return sum
print(FMN(a,n))

# Approch 2 O(n) sc=O(1) it doesnt have overflow
#XOR based
a=[1,9,3,7,6,5,4,8,2]
def FMN2(a,n):
    x1, x2 = a[0], 1
    for i in range(1,n):
        x1 ^= a[i]
    for i in range(2, n+2 ):
        x2 ^=i
    return x1 ^ x2
FMN2(a,len(a))

def FMN3(a):
    x1 = 0
    x2 = 0
    for i in range(1,len(a)+2):
        x1 ^= i
    for i in range(len(a)):
        x2 ^= a[i]
    return x1 ^ x2

print(FMN3(a))