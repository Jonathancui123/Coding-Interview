# Idea: Reachable indices will be contiguous from the first index => don't need to mark "jumpable", simply remember the furthest jumpable index
# Note: Be careful about EDGE cases (e.g. 1 elem in array) Walk through your code to make sure there's no errors

# Initially: Can be done through backtracking through each jumpable pattern or using DP

# Use (Bottom-up) DP to mark each position as reachable or not. For each reachable position, mark the indices within range as reachable as well
# O(n^2) time, O(n) space

# initalialize maxJumpable (int) = 0
# Iterate through each index of the array until (index > maxjumpable OR index > len(array) - 1)
    # On each index, add the value of the elem to the current index and update maxJumpable if needed

# O(n) time, O(1) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currIndex = 0
        maxJumpable = 0
        while(currIndex <= maxJumpable and currIndex <= len(nums) -1):
            maxJumpable = max(maxJumpable, currIndex + nums[currIndex])
            currIndex += 1 
            
        if (currIndex > len(nums) -1):
            return True
        else:
            return False