'''Given a binary array nums, return the maximum number of consecutive 1's in the array.'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        curr = 0
        for ele in nums:
            if ele:
                curr+=1        
            else:
                curr = 0
            count = max(curr, count)
        return count
                                    
    
if __name__ == "__main__":
    obj = Solution()
    barray = [0,0,1,1,0,1,1,0]
    print(obj.findMaxConsecutiveOnes(barray))