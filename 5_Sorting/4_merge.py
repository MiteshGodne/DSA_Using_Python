def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid+1
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])            
            right+=1
    while right <= high:
        temp.append(arr[right])
        right+=1
    while left <= mid:
        temp.append(arr[left])
        left+=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]
        
def merge_sort(arr: int, low: int, high: int):
    if low >= high:
        return 
    mid = low + ((high-low)//2)
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
arr = [1,3,6,2,2,8,2,8,0,-1,102]
merge_sort(arr, 0, len(arr)-1)
print(arr)
        
