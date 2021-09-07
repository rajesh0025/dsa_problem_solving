# A number is a leader if all nums in right side should not be greater than it in an array
#Brute force approch1 --- O(n^2), sc=O(1)
arr = [8,4,2,3,1,5,4,2]
#output = [8,5,4,2]

#best Approch2 O(n), sc O(1)
#traverse from right to left
a=[8,4,2,3,1,5,4,2]
n=len(a)
x=[]
current_max = -float("inf")

for i in range(n-1,-1,-1):
 if a[i]>current_max:
  x.append(a[i])
  current_max=a[i]
""" if i== n-1:
  x.append(a[i])
 if a[i] > x[-1]:
  x.append(a[i]) 
"""  
print(x)
    

