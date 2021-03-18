# nums = [3,2,3,9] --> 12

# (TOP DOWN DP example)
# i = 3
# rob = prevNotRobbed + nums[i]
# notRob = max(prevNotRobbed, prevRobbed)

# prevRobbed = 12
# prevNotRobbed = 6

# TOP DOWN RECURSIVE SOLUTION
# For an index i:
#     return max of 
#         1. [we rob this index] --> nums[i] + rob(nums[i+2:])
#         2. [we dont rob this index] --> rob(nums[i+1:])
# i = 0
# 1. 3 + 9
#         i = 2
#         1. 3 + 0
#                 i = 4
#                 END: 0
#         2. 9
#             i = 3
#             1. 9
#                     i = 5
#                     END: 0
#             2. 0
#                 i = 4
#                 END: 0
# 2. 
# # O(2^n) time and O(n) space

# Top down DP:
# - Memoize the max robbable amount for each index (and beyond) into an array 
# - O(n) time, O(n) space

# Bottom up DP:
# - At each index, generate the max robbable for this index and all houses to the left, given:
#     1. we rob this house        (--> prevRobbed)
#     2. we dont rob this house   (--> prevNotRobbed)

#     1. nums[i] + maxWithPreviousRobbed
#     2. nums[]
# O(n) time, O(1) space
    
class Solution:
    def rob(self, nums) -> int:
        rob = 0
        notRob = 0
        
        prevRobbed = 0
        prevNotRobbed = 0
        for num in nums:
            rob = prevNotRobbed + num
            notRob = max(prevRobbed, prevNotRobbed)
        
            prevRobbed = rob
            prevNotRobbed = notRob
        
        return max(rob, notRob)
        
        