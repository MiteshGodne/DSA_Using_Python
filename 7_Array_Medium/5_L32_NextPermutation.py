'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order.For example, for nums = [1,2,3], the following are all the permutations of array: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. '''

class Solution:
    def nextPermutation_v1(self, nums: list[int]) -> None:
        all_perms = self.generate_permutation(nums)
        for i in range(len(all_perms)):
            if all_perms[i] == nums:
                nums[:] = all_perms[i+1] if i+1 < len(all_perms) else all_perms[0]
                return
                
    def generate_permutation(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]
        perms = []
        for i in range(n):
            elem = nums[i]
            remains = nums[:i] + nums[i+1:]
            for perm in self.generate_permutation(remains):
                if [elem]+perm not in perms:
                    perms.append([elem]+perm)
        return perms
        
if __name__ == '__main__':
    obj = Solution()
    nums = [2,1,5,4,3,0,0]
    obj.nextPermutation_v1(nums)
    print(nums)
    