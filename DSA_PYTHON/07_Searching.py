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
    if low <= high:
        mid = (low + high)//2
        if item == arr[mid]:
            return mid 
        elif arr[mid] > item:
            return Binary_search(arr,low,mid-1,item)
        else :
            return Binary_search(arr,mid+1,high,item)
    else :
        return -1

def Binary_search_loop(arr, low, high, item):

    while low <= high:

        mid = (low + high) // 2
        print(mid)

        if arr[mid] == item:
            print(mid, "in if statement")
            return mid

        elif arr[mid] > item:
            print(mid, "in elif statement")
            high = mid - 1

        else:
            print(mid, "in else statement")
            low = mid + 1

    return -1

arr2 = [10,22,33,44,54,66,79,90,99,100]
ans = Binary_search_loop(arr2,0,(len(arr2)-1),99)
print(ans)

def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
            return sorted
    return sorted
 
print(is_sorted(arr2))

def Bubble_sort(arr):
    flag = 0
    for i in range(len(arr) - 1) :
        flag = 0
        print("pass ",i)
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        if flag == 0 :
            return arr
    return arr
print(Bubble_sort([6,1,2,3,4,5]))