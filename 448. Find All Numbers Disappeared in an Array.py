# CYCLICE SORT, ARRAY, (Use indices to represent numbers)

# Ex 1: [3,3,3] -> [1,2]

'''
O(n^2) time [brute] : For each number in [1, n], check if it is in nums. If it is not, add it to the output list
O(n) time, O(n) space [set]: Create a set initialized to contain [1,n] and remove each element that we see in nums. 
    Or use a boolean list of size n initialized to False, and set index i - 1 to true if i is found/
    We go through the set or the list and populate the final solution
O(n) time, O(1) 'extra' space: Cyclic sort to put each number, i, into index i-1. If the duplicate already exists in i-1, let it rest in the current position --> Each index will hold the number (index + 1) if (index + 1) exists.
    Iterate through nums and find indices that don't hold index + 1 
ANOTHER SOLUTION: Since each index can be one-to-one mapped to a number, and all numbers were positive, simpy set an index to negative to mark the number as found. Return the numbers represented by indices where the element is unmarked
    
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        cycleStartIndex = 0
        
        while cycleStartIndex < len(nums):            
            temp = nums[cycleStartIndex]
            currentIndex = temp - 1
            
            while temp != cycleStartIndex + 1 and nums[currentIndex] != temp:
                nextTemp = nums[currentIndex]
                nums[currentIndex] = temp
                temp = nextTemp
                currentIndex = temp - 1
                
            
            nums[cycleStartIndex] = temp           
            cycleStartIndex += 1
        
        result = []
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i+1)
                
        return result