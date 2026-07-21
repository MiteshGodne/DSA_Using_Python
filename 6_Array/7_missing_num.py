# Given an array[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

def missing(nums):
    sum = 0
    n = len(nums)+1
    for ele in nums:
        sum+=ele
    return n*(n+1)//2 - sum

def missing_xor(nums):
    n = len(nums)+1
    arr = [i for i in range(1, n+1)]
    res = 0
    for ele in nums:
        res^=ele
    for ele in arr:
        res^=ele
    return res

array = [-1,-2,-3,-5]
print(missing(array))
print(missing_xor(array))