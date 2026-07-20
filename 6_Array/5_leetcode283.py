'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.'''

class Solution:
    def moveZeroesBrute(self, nums: list[int]) -> None:
        n = len(nums)
        i = j = 0
        while i<n and j<n:
            while i<n:
                if not nums[i]:
                    break
                i+=1
            while j<n:
                if nums[j]:
                    break
                j+=1
            if i < j and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1
            
if __name__ == "__main__":
    obj = Solution()
    arr = [1,0,0,0,0,3]
    obj.moveZeroesBrute(arr)
    print(arr)