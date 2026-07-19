'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. Do not return anything, modify nums in-place instead.'''

class Solution:
    def rotate_brute(self, nums: list[int], k: int) -> None:
        k%=len(nums)
        for i in range(k):
            temp = nums[-1]
            for j in range(-1,-len(nums), -1):
                nums[j] = nums[j-1]
            nums[0] = temp
        
if __name__ == "__main__":
    obj = Solution()
    arr = [1,2,3]
    obj.rotate_brute(arr, 4)
    print(arr)