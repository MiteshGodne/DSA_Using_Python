def insertion_sort(arr: int):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i-1
        while prev >= 0 and arr[prev]>curr:
            arr[prev+1] = arr[prev]
            prev-=1
        arr[prev+1] = curr
            
arr = [1,3,6,2,2,8,2,8,0,-1,102]
insertion_sort(arr)
print(arr)