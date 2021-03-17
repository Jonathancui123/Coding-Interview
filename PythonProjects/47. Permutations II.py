class Solution:
    def backtrack(self, nums, used, currentPermutation, output):
        # a permutation has been fully built
        if (len(currentPermutation) == len(nums)):
            output.append(currentPermutation.copy())
            return

        i = 0
        while i < len(nums): 
            if not used[i]:
                used[i] = True
                currentPermutation.append(nums[i])
                self.backtrack(nums, used, currentPermutation, output)
                currentPermutation.pop()
                used[i] = False

                currentElem = nums[i]
                while (i < len(nums) and nums[i] == currentElem):
                    i += 1
                    
            else :
                i += 1
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        output = []
        currentPermutation = []
        
        self.backtrack(nums, used, currentPermutation, output)
        return output

    

        return output