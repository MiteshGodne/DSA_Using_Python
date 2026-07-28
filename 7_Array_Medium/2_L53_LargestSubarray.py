'''Given an integer array nums, find the subarray with the largest sum, and return its sum.'''
class Solution:
    def maxSubArray_v1(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            running_sum = 0
            for j in range(i, n):
                running_sum+=nums[j]
                if running_sum > max_sum:
                    max_sum = running_sum
        return max_sum
    
if __name__ == '__main__':
    obj = Solution()
    nums = [-2,-3,4,-1,2,1,5,-4]
    print(obj.maxSubArray_v1(nums))