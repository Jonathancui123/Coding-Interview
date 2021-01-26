# Searching for targets in a sorted array -> use binary search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:       
        # Inclusive bounds for our search area
        leftBound = 0
        rightBound = len(nums) - 1
        
        # First binary search to find any element that matches the target
        while(leftBound <= rightBound):
            midPoint = (leftBound + rightBound)//2
            if (nums[midPoint] == target):
                # Perform further searching to find the starting and ending position of the target value
                return Solution.searchBounds(leftBound, rightBound, midPoint, nums, target)
                
            elif nums[midPoint] < target:
                leftBound = midPoint + 1
            else:
                rightBound = midPoint -1
        
        return [-1, -1]
    
#     assumes that the original midpoint represent an instance of the target in a sorted array
# returns the starting position and ending position of the target value
    def searchBounds(originalLeftBound, originalRightBound, originalMidPoint, nums, target):
        startPosition = -1
        endPosition = -1
        # Look for the starting position of the target
        leftBound = originalLeftBound
        rightBound = originalMidPoint
        while(leftBound <= rightBound):
            midPoint = (leftBound + rightBound)//2
            if (nums[midPoint] == target and (midPoint == 0 or nums[midPoint - 1] != target)):
                startPosition = midPoint
                break
            elif (nums[midPoint] != target):
                leftBound = midPoint + 1
            else:
                rightBound = midPoint - 1

        leftBound = originalMidPoint
        rightBound = originalRightBound

        while(leftBound <= rightBound):
            midPoint = (leftBound + rightBound)//2
            if (nums[midPoint] == target and (midPoint == len(nums)-1 or nums[midPoint + 1] != target)):
                endPosition = midPoint
                break
            elif (nums[midPoint] != target):
                rightBound = midPoint - 1
            else:
                leftBound = midPoint + 1

        return [startPosition, endPosition]
    