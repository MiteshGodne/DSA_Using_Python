'''Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

class Solution:
    def majorityElement_v1(self, nums: list[int]) -> int:         # O(NlogN) & O(N) space for timsort internally
        nums.sort()
        return nums[len(nums)//2]           
    
    def majorityElement_v2(self, nums: list[int]) -> int:         # O(N) & O(N)
        from collections import Counter
        counts = Counter(nums)
        return counts.most_common(1)[0][0]
    
    def majorityElement_v3(self, nums: list[int]) -> int:          # O(N) & O(1)
        count = 0
        maj_ele = 0
        for num in nums:
            if count==0:
                maj_ele = num
            if maj_ele == num:
                count+=1
            else:
                count-=1
        return maj_ele
        
if __name__ == "__main__":
    obj = Solution()    
    nums = [10,3,5,3,10,10,10]
    print(obj.majorityElement_v1(nums))
    print(obj.majorityElement_v2(nums))
    print(obj.majorityElement_v3(nums))
