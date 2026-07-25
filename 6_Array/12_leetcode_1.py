class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[nums[i]] = i
        return [-1,-1]
            
if __name__ == "__main__":
    obj = Solution()    
    nums = [7,2,3,5,3,0,10,10]
    print(obj.twoSum(nums, 6))
