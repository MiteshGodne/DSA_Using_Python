# Hashing -> TC:O(N * log N) + SC:O(N) -> also for negatives   
def longest_subarray(nums : list[int], k: int) -> int:
    prefix_sum = {0: -1}
    n = len(nums)
    length = 0
    csum = 0
    for i in range(n):
        csum+=nums[i]
        idx = prefix_sum.get(csum - k)
        if idx is not None:
            length = max(length, i-idx)
        if csum not in prefix_sum:
            prefix_sum[csum] = i
    return length           
 
nums = [5,5,5,12,5,10,-8,0,0,3,-10,20,5,5]
print(longest_subarray(nums, 15))