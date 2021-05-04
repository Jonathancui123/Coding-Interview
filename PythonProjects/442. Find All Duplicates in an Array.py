'''
O(n^2) brute
O(nLogn) sort
O(n) time and O(n) space hashmap/set

O(n) time O(1) space --> 
1. [Index indicator w/ negatives] For each element, n, "mark" index n - 1 by making it negative to show that n has been seen. The second time we try and mark a number, that must mean it is duplicated.
2. [Cyclic sort] We perform a modified cyclic sort. On the second time a number should be put into the index, we record this number as having a duplicate, and place it at the beginning of the cycle. To avoid recording a duplicate multiple times, we set the duplicate at the proper index to be negative after recording it the first time. 
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        currIndex = 0
        while currIndex < len(nums):
            elem = abs(nums[currIndex])
            
            if currIndex + 1 != elem:
                #  elem does not belong to current index                
                if abs(nums[elem - 1]) != elem:
                    #  the number in the proper index isn't a duplicate, swap
                    nums[elem-1], nums[currIndex] = nums[currIndex], nums[elem-1]  
                else:
                    # There is a duplicate in the proper index
                    if nums[elem - 1] > 0: 
                        # The duplicate hasn't been recorded yet
                        nums[elem - 1] = -nums[elem - 1]
                        duplicates.append(elem)
                    currIndex += 1
            else:
                # elem belongs at the current index
                currIndex += 1
                
        return duplicates