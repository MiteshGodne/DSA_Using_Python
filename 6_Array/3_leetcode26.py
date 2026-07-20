'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.'''

class Solution:
    def remove_duplicates(self, nums):
        if len(nums) == 0:
            return 0
        k = 1
        curr = nums[0]
        for i in range(len(nums)):
            if curr != nums[i]:
                nums[k] = nums[i]
                curr = nums[i]
                k+=1
        return k
    
    def remove_duplicates_v2(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k+=1
        print(nums)
        return k
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.remove_duplicates_v2([-100,2,4,6,6,6,8,9,9]))
            
