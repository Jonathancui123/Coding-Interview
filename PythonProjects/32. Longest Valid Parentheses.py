32. Longest Valid Parentheses

# Brute force: For each index of the string, consider it the starting point of a substring, check how long the longest valid substring starting at this starting point
# Valid substring: There have never been more closing brackets than opening brackets at any point in the substring. There are the same number of closing and opening brackets
# --> O(n^2) time, possibly using a stack for O(n) space

# The above repeats a lot of work by looking at the same parentheses multiple times

# Idea: Using a stack for the entire string at once requires that we know how many characters are between each pair of matching parentheses
# --> Use a stack that stores (parenthesis, index) as a tuple. Closing a pair of parentheses and popping it off the stack means that we have a series of valid parentheses between the index of the new top of stack and the current index

# Ex:
# ")()())(())"


# currentIndex = 9
# longestValid = 4
# indexOfStackBottom = 5

# indexOfStackBottom is changed to the current index if we see a closing parenthesis when the stack is empty

# O(n) time, O(n) space

from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        indexOfStackBottom = -1
        longestValid = 0
        parenthesisStack =  deque()
        
        for i in range(len(s)):
            if s[i] == "(":
                parenthesisStack.append(i)
            elif len(parenthesisStack) == 0:
#               Closing parenthesis, stack is empty --> invalid substring
                indexOfStackBottom = i
            else:
#               Closing parenthsis, stack is non-empty --> valid substring
                if len(parenthesisStack) == 1:
                    parenthesisStack.pop()
                    validSubstringLength = i - indexOfStackBottom
                else:
                    parenthesisStack.pop()
                    validSubstringLength = i - parenthesisStack[-1]
                longestValid = max(longestValid, validSubstringLength)
        return longestValid
            
            
# NOTE: Try and use deque[-1] instead of .peek()
                
                
                