# import array
from array import *
val = array('i',[1,2,3,4,5,6])
print(val)

for i in range(0,6):
    print(val[i],end=" ")
print("\n")
for x in val:
    print(x)


## Methods in array 

#len() // to know the len 
#typecode to know the typecde 
# to reverse the arr reverse()
# inasert(inx,value)
arr2 = array('i',[])
arr = array('i',[1,2,3,4,5,6,77,8,9])
for i in arr :
    arr2.insert(0,i)
print(arr2)

## copy arr
copyarr = array(arr.typecode,(x*3 for x in arr ))

print(copyarr)

## slicing in array 

abc = arr[2:5]#reverse by slicing [::-1]
for i in range(0,len(abc)):
    print(abc[i],end=" ")

# ## user input from array 
# n = int(input("Enter the input : "))
# nums = array('i',[])
# for i in range(n):
#     nums.append(int(input("Enter the nums : ")))
# for i in nums:
#     print(i , end=" ")

index = array('i',[24,321,45,5332,1,334,2221,54,])
i = index.index(54)
print("\nThis is the ", i) 