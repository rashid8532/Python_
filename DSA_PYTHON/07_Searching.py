# This is linier_search 

def linier_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = [12,33,45,77,100,104,99,92]
ans = linier_search(arr,99)
print(ans)

# This is Binary_search 
def Binary_search(arr,low,high,item):
    mid = (low + high)//2
    if item == arr[mid]:
        return mid 
    elif arr[mid] < item:
        return Binary_search(arr,low,mid-1,item)
    else :
        return Binary_search(arr,mid+1,high,item)
    return -1

arr2 = [10,22,33,44,54,66,79,87,99,100]
ans = Binary_search(arr2,0,len(arr2) - 1,44)
print(ans)

