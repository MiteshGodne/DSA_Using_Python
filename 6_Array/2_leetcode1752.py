'''Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.'''

class Solution:
    # Brute Force
    def check_brute(self, nums: list[int]) -> bool:
        n = len(nums)
        arr = nums.copy()
        arr.sort()
        posi = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                posi = i+1
        for i in range(n):
            if arr[i] != nums[posi]:
                return False
            posi = (posi+1)%n
        return True
    
    # Optimized
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        drops = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drops += 1 
                if drops > 1:
                    return False
        return True
            
if __name__ == '__main__':
    obj = Solution()
    nums = [1]
    print(obj.check(nums))