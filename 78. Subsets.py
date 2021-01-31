# Implemented: Backtracking to try each nums at each position. Build up a templist and commit it to the solution at each call of the backtracking function. (We ensure uniqueness and correctness of subsets by not using a number after it has been skipped/already used). Upon analysis of the backtracking tree, we notice that a node with n+1 elements left in nums, has double the child nodes as a node with n elements left in nums. Thus, there are O(2^n) nodes in the backtracking tree which each take O(n) time to build/copy. O(n*(2^n)) time and space.
# Alternative (better): Each num is either included/excluded in each subset. For each num in nums, commit a duplicate of all existing subsets and include the num. O(2^n) subsets each taking O(n) to build/copy --> O(n*(2^n)) time complexity, and O(n*(2^n)) space for the final array

# Note: watch out for the edge case - how to handle the empty subset? subset containing all nums? when to commit a tempList to solutions?
# --> commit the templist at the beginning of each backtracking call. This will commit the empty set (since the first call is with an empty set), as well as the subsets after the last element has been selected (and the for loop won't run in these cases)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        tempList = []
        Solution.backtrack(nums, 0, tempList, solution)
        return solution
        
    def backtrack(nums, startIndex, tempList, solution):
        solution.append(tempList[:])
        
        for i in range(startIndex, len(nums)):
            tempList.append(nums[i])
            Solution.backtrack(nums, i + 1, tempList, solution)
            tempList.pop()
        
        