# Idea: To produce all UNIQUE combinations from a pool of non-unique candidates, we need to  backtrack with each possible quantity (zero to all) of each unique candidate. Do this by keeping a hashmap of counts or sorting, counting occurences, and skipping to the next unique element. 

# No need to sort the array
# Implementation 1: Use a hashmap (O(n) space and time) to record how many of each candidate we have. Do backtracking: Build up a combination that could sum to target using backtracking over a different amount of each unique candidate up to the quantity available.  

# For each combination, each individual candidate is either included/excluded from the combination
# Implementation 2: Sort the candidates. For each unique candidate, check how many of that candidate there are in the candidate pool by iterating forward, backtrack with each possible quantities (zero to all). If the running sum of the combination is greater than target, kill that combination. If it equals zero, then commit that combination to the solution. Repeat for each unique candidate.

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = Counter(candidates) # O(n)
        uniqueCandidates = list(set(candidates)) # O(n)
        combinations = []
        tempCombo = []
        Solution.backtrack(uniqueCandidates, 0, counts, combinations, target, tempCombo)
        return combinations
        
    def backtrack(uniqueCandidates, currIndex, counts, combinations, target, tempCombo):
        if (target == 0):
            combinations.append(tempCombo[:])
            return
        elif (target < 0):
            return  
        elif (currIndex >= len(uniqueCandidates)):
            return
        else:
            currCandidate = uniqueCandidates[currIndex]
            for i in range(counts[currCandidate] + 1):
                for j in range(i):
                    tempCombo.append(currCandidate) 
                newIndex = currIndex + 1
                newTarget = target - (currCandidate * i)
                Solution.backtrack(uniqueCandidates, newIndex, counts, combinations, newTarget, tempCombo)
                for j in range(i):
                    tempCombo.pop()
            return
                
                
        