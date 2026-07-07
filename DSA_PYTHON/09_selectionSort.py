def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)

a = [2,5,3,2,15,32,35,64,37,88]
selectionSort(a)