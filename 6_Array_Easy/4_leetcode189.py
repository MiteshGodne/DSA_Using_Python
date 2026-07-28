'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. Do not return anything, modify nums in-place instead.'''

class Solution:
    def rotate_brute(self, nums: list[int], k: int) -> None:
        k%=len(nums)
        for i in range(k):
            temp = nums[-1]
            for j in range(-1,-len(nums), -1):
                nums[j] = nums[j-1]
            nums[0] = temp
    
    # Optimized
    def my_rev(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
    def rotate_v2(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if k<=0:
            return 
        k%=n
        self.my_rev(nums, 0, n-k-1)
        self.my_rev(nums, n-k, n-1)
        self.my_rev(nums, 0, n-1)
        
    # Optimized using slice operator
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k%=n
        if k<=0:
            return
        nums.reverse()        
        nums[:k] = reversed(nums[:k])
        nums[k:n] = reversed(nums[k:n])
        
if __name__ == "__main__":
    obj = Solution()
    arr = [1,2,3]
    obj.rotate_brute(arr, 4)
    obj.rotate_v2(arr, 4)
    print(arr)