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
             
    # Dutch National Flag Algorithm - 3 pointers and 4 parts of array (0 to low-1 = zeros, low to mid-1 = ones, mid to high = unsorted, high+1 to n = twos)
    def sortColors_v2(self, nums: list[int]) -> None:
            low, mid, high = 0, 0, len(nums)-1
            while mid <= high:
                if nums[mid] == 0:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low+=1
                    mid+=1
                elif nums[mid] == 1:
                    mid+=1
                else:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high-=1
    
if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,0,1,0,1]
    obj.sortColors_v1(nums)
    print(nums)
    obj.sortColors_v2(nums)
    print(nums)