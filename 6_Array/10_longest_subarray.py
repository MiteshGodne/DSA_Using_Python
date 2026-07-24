# Brute Force - O(n^2) -> Only for Non negatives
def longest_subarray_v1(nums : list[int], k: int) -> int:
    n = len(nums)
    length = 0
    for i in range(n):
        prefix_sum = 0
        for j in range(i, n):
            prefix_sum+=nums[j]
            if prefix_sum==k:
                length = max(length, j-i+1)
    return length     

nums = [5,5,12,5,10,5,5,5,9]
print(longest_subarray_v1(nums, 15))