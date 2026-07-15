def partition(arr, low, high):
    pivot = arr[low + (high-low)//2]         # hoarse technique
    i, j = low-1, high+1
    while i < j:
        while True:
            i+=1
            if arr[i] >= pivot:
                break
        while True:
            j-=1    
            if arr[j] <= pivot:
                break
        if i>=j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
    return j
    
def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p+1, high)
    
arr = [1,3,6,2,2,8,2,8,0,-1,102]
quick_sort(arr, 0, len(arr)-1)
print(*arr)
        