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