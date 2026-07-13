def bubble_sort(arr: int):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
        if not swapped:
            break    
               
arr = [1,3,6,2230,5432,85,2,-8,40]
bubble_sort(arr)
print(arr)