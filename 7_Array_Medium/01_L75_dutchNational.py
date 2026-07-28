'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.'''
class Solution:
    def sortColors_v1(self, nums: list[int]) -> None:
        zeroes = ones = twos = 0
        n = len(nums)
        for ele in nums:
            if ele == 0:
                zeroes+=1
            elif ele == 1:
                ones+=1
            else:
                twos+=1
        i = 0
        for i in range(zeroes):
             nums[i] = 0
        for i in range(zeroes,zeroes+ones):
             nums[i] = 1
        for i in range(zeroes+ones, n):
             nums[i] = 2
    
if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,0,1,0,1]
    obj.sortColors_v1(nums)
    print(nums)