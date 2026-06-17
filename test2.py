arr = [1,2,0,3,0,4,0,5,6]
for i in arr:
    if i == 0:
        arr.remove(i)
        arr.insert(-1,i) 
print(arr)