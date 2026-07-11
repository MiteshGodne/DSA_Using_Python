def selection_sort(arr: int):
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            min = j if arr[j] < arr[min] else min
        if min != i:
            arr[i],arr[min] = arr[min],arr[i]
            
arr = [1,3,6,2,2,8,2,8,0]
selection_sort(arr)
print(arr)