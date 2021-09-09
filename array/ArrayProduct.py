"""Problem Statement:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].



Example:





Input:  [1,2,3,4]

Output: [24,12,8,6]

"""
#Approch1 brute force --- O(n) , sc=O(1)
a = [1,2,3,4]
out = []
for i in range(len(a)):
    count = 1
    for j in range(len(a)):
        if i==j:
            count *1
        else:
            count *= a[j]
    out.append(count)
print(out)

#Approch2 =O(n) , additional space

a = [4,5,1,8,2,10,6]
l = [1]
r = [1]
for i in range(len(a)-1):
    l.append(a[i] * l[i])
for i in range(len(a)-1,0,-1):
    r.append(a[i]*r[len(a)-1-i])
out =[]
for i in range(len(r)):
    out.append(l[i]*r[len(r)-i-1])

print(out)

a = [1,2,3,4]
l = [1]
r = [1]
for i in range(len(a)-1):
    l.append(a[i] * l [i])
for i in range(len(a)-1,0,-1):
    r.append(a[i]*r[len(a)-1-i])
out =[]
for i in range(len(r)):
    out.append(l[i]*r[len(r)-i-1])

print(out)

# BestApproch O(n), nospace
a = [1,2,3,4]
out = [1]
for i in range(len(a)-1):
    out.append(a[i] * out[i])
r=1
for i in range(len(a)-1,-1,-1):
    out[i] = out[i]*r
    r*=a[i]
print(out)


        

