'''You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.You should return the array of nums such that the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.'''

class Solution:
    def rearrangeArray_v1(self, nums: list[int]) -> list[int]:
        n = len(nums)
        posi = []
        nega = []
        for num in nums:
            nega.append(num) if num < 0 else posi.append(num)
        for i in range(n//2):
            nums[2*i] = posi[i]
            nums[2*i+1] = nega[i]
        return nums
    
    def rearrangeArray_v2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0]*n
        posi = 0
        nega = 1
        for i in range(n):
            if nums[i] < 0:
                res[nega] = nums[i]
                nega+=2
            else:
                res[posi] = nums[i]
                posi+=2
        return nums
        
if __name__ == '__main__':
    obj = Solution()
    nums = [3,1,-2,-5,2,-4]
    print(obj.rearrangeArray_v1(nums))
    print(obj.rearrangeArray_v2(nums))