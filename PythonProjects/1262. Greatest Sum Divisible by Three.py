# [3,6,5,1,8]
# [8,6,5,3,1] = 23,     23 % 3 = 2
# [8,6,5,3] = 22,     22 % 3 = 1
# [8,6,5] = 22,     22 % 3 = 1

1. Sort the array, sum the elements and see what the remainder is mod 3
- We want to remove the minimum value of elements from this array such that the remainder mod 3 becomes zero
----
Idea: Each element is either removed or not removed from the array. Try each possibility recursively
To calculate the minimum value of elements we must remove:
2. Starting from the small side of the array, mark the element as removed by adding it to a list of "removed" elements.
3. Calculate the new remainder of the sum after it has been removed. And recurse on the remainder of undecided numbers.
(Unremove the element)
4. Recurse on the remainder of undecided numbers. Without removing the current element.
5. Return the minimum of the values returned from both recursive calls (If both calls returned numbers).
- base case 1: remainder is 0 --> return the current sum of the "removed" list
- base case 2: no undecided elements left and non-zero remainder --> return None to signify that the current collection of removed numbers cannot lead to a zero remainder situation

remainder 1:
remove [1], [2] + [2]
remainder 2:
remove [1] + [1], [2]

If the sum of all the numbers is non-zero:

In a single pass, keep track of the two smallest [1], [2]. O(n)

For remainder 1:
    - if we don't have [1] and we don't have two [2], it is impossible to fix
    - calculate whether it is cheaper to remove the [1] or if it is cheaper to remove the two [2]. If either option is undefined then used the defined option.

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        if (totalSum % 3 == 0):
            return totalSum
        else:
#           index zero is the smallest, index one is the second smallest
            smallestRemainder1 = [None, None]
            smallestRemainder2 = [None, None]
            
            for num in nums:
                if (num % 3 == 1):
                    if (smallestRemainder1[0] == None or num < smallestRemainder1[0]):
                        smallestRemainder1[1] = smallestRemainder1[0]
                        smallestRemainder1[0] = num
                    elif (smallestRemainder1[1] == None or num < smallestRemainder1[1]):
                        smallestRemainder1[1] = num
                    
                elif (num % 3 == 2):
                     if (smallestRemainder2[0] == None or num < smallestRemainder2[0]):
                        smallestRemainder2[1] = smallestRemainder2[0]
                        smallestRemainder2[0] = num
                    elif (smallestRemainder2[1] == None or num < smallestRemainder2[1]):
                        smallestRemainder2[1] = num
            
            if (totalSum % 3 == 1):
                if(smallestRemainder1[0] == None and (smallestRemainder2[0] == None or smallestRemainder2[1] == None)):
                    return 0
                elif (smallestRemainder1[0] == None):
                    return totalSum - smallestRemainder2[0] - smallestRemainder2[1]
                elif (smallestRemainder2[0] == None or smallestRemainder2[1] == None):
                    return totalSum - smallestRemainder1[1]
                else:
                    return totalSum - min(smallestRemainder1[0], smallestRemainder2[0] + smallestRemainder2[1])
                
            else:
                if(smallestRemainder2[0] == None and (smallestRemainder1[0] == None or smallestRemainder1[1] == None)):
                    return 0
                elif (smallestRemainder2[0] == None):
                    return totalSum - smallestRemainder1[0] - smallestRemainder1[1]
                elif (smallestRemainder1[0] == None or smallestRemainder1[1] == None):
                    return totalSum - smallestRemainder2[1]
                else:
                    return totalSum - min(smallestRemainder2[0], smallestRemainder1[0] + smallestRemainder1[1])
        
    def 