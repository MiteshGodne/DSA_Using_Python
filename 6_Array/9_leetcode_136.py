'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for ele in nums:
            xor^=ele
        return xor                    
    
if __name__ == "__main__":
    obj = Solution()
    nums = [0,1,2,2,1,5,5,3,3,-7,8,8]
    print(obj.singleNumber(nums))