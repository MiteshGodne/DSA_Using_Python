def missing(nums):
    sum = 0
    n = len(nums)
    for ele in nums:
        sum+=ele
    return sum - n*(n+1)//2

print(missing([1,2,3,5,6]))