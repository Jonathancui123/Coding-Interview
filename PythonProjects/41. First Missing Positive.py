# CYCLIC SORT, ARRAY

'''
 Insight 1: The solution must be within [1, n+1], all other values can be trashed/disregarded

 Insight 2: We can use array positions/indices to map to numbers between [1,n+1] (Index 0 refers to number 1, number = index + 1)

 Two possible strategies:

 1. Use cyclic sort to place numbers between [1, n] into indices [0, n - 1]. 
 Values less than 1, or greater than n are not intentionally moved. 
 Iterate over the sorted array to find the first missing positive.
 
 2. 
 Remove all numbers outside of [1, n] by setting them to n + 1. (n + 1 is a positive number that is the default solution if all [1, n] are found)
 Iterate through the array, and consider each element 'i'. Set nums[i - 1] to be negative if: 0 < i < n + 1
 Iterate through the array and find the first non-negative element - at position i - 1. i is the missing element
 If no positive elements are found, then [1, ...,  n] is the original array and the first missing positive is n + 1

 '''