'''Given an array, find the second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.'''

def find_second_largest(arr):
    if len(arr) < 2:
        return -1
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num
    return second_largest if float('-inf') != second_largest else -1

arr = [6,9,6,9,10,2,9,2]
print(find_second_largest(arr))
            
        
        