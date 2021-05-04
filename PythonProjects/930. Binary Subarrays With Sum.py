930. Binary Subarrays With Sum

Brute force: Use 2 pointers to iterate over all possible possible subarrays and sum it --> O(n^3)

Idea: We want the sum of subarrays, so a prefix sum array will allow us to find these sums in O(1) after O(n) time/space for creating the sum array
--> after creating the prefix sum array, create a hashmap that shows how many of each sum we have. Multiply the counts in this hashmap that are S apart to identify how many subarrays with Sum.

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Examples:
A = [1,0,1,0,1,1], S = 2
Output: 4

1. 0 -> 2
2. 0 -> 3
3. 1 -> 4
4. 2 -> 4

Example #2:
[0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], S = 3
[0, 0, 0, 1, 2, 3, 3, 3, 4, 4, 5] L Cumulative array: Cumulative sum at the current position and to the left

ans = 1 + 3 + 3 + 3 + 1 + 1 + 1

{
	 3: 3,
   4: 1,
   5: 1,
   6: 3,
   7: 2,
   8: 1,
}

Hashmap: {Cumulative sum -> # of times we stay at that cumulative sum}

- Keys in this map will be consecutive starting from 0 or 1
- Loop from i =0 or i=1 until i is no longer in the hashmap
for each i:
- multiply hashmap[i] and hashmap[i+S]

i = 0
hashmap[i] = 3
hashamp[i+S] = 3
--> 3 x 3 = 9

if S = 0:
- Don't do multiplication, just increment by hashmap[i]

O(n) time O(n) space to construct this hashmap
O(n) time to loop through the hashmap

Sum between i, j:  S[i, j] = cumu_sum[:j] - cumu_sum[:i]
										S + cumu_sum[:i] = cumusum[:j]

Output: 6

Example #3:
[0,0,1,0,0], S = 1

Example #4:
[0,0,0] S=0
--> Any subarray is valid


- A might be empty
- S could be 0, but always positive

n = length of A

Brute Force:
- Determine start and stopping points of all possible (non-empty) subarrays O(n^2)
- For each subarray, check if it sums to S O(n)
	- If it does, increase a counter that tracks how many subarrays sum to S O(1)
  
--> O(n^3) time, O(1) space

Optimizing:
- Unecessary work: considering subarrays that definitely have sum greater than S
- Duplicated work: Recalculating the sum each time

Idea: Sliding window

- Keep a counter of subarrays that sum to S
- Keep track of the running sum in the window
- As long as moving the right pointer doesn't bring the sum of the window above S, move the pointer to the right
	- Each time the window changes, update the running sum by incrementing/decrementing the running sum by 1 or 0
	- Each time the window changes, if the sum is equal to S, incrememt the counter
- Otherwise, move the left pointer forwards
	- Each time the window changes, update the running sum by incrementing/decrementing the running sum by 1 or 0
	- Each time the window changes, if the sum is equal to S, increment the counter

--> need to consider 0's on the window edge

Examples:
A = [1,0,1,0,1], S = 2
Output: 4

1. 0 -> 2
2. 0 -> 3
3. 1 -> 4
4. 2 -> 4











.