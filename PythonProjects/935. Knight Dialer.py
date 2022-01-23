935. Knight Dialer

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). 
The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

<photo>

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo (10^9 + 7).

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.



Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]


Input: n = 3
Output: 46

Input: n = 4
Output: 104

Brute force: 
Recursive -->

possibleJumps = {
  0: [4, 6],
  1: [6, 8],
  2: [7, 9],
  3: [4, 8],
  4: [3, 9, 0]
  5: []
  6: [1, 7, 0]
  7: [2, 6]
  8: [1, 3]
  9: [2, 4]
}
--> NOTE: possibly save space: 0->4 indicates that 4->0

- n is the depth our recursion

- at each level, i, from 0 to n: build up a list of all unique possible strings of length i
--> to get to i + 1: take each unique string from the previous level, and add a new string for each possible jump from the final number of the length i string

Time: O(3^n * n)
Space: O(3^n * n)

--> computing all unique strings might unecessary because we only want to know how many unique strings are possible

----------------------------------------------------------------

-->  at each length i, from 0 to n, track the number of strings that end in the value 0, the value 1, ... ec,

O(1) size
stringsEndingIn = {
	0: 1,
  1: 1,
  ..
  9: 1,
}

- at length 1: there is 1 string ending at each value
- to get from length i, to length i+1,:
	- create a new hashmap for i+1, for each number in the level i hashmap mapping to the value x, increment the entries that the number can jump to in the i+1 hashmap by x
	- O(1) operation --> always 10 numbers, which jump to 0-4 other numbers
  
O(n) time
O(1) space 

i = 2
[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

possibleJumps = {
  0: [4, 6],
  1: [6, 8],
  2: [7, 9],
  3: [4, 8],
  4: [3, 9, 0]
  5: []
  6: [1, 7, 0]
  7: [2, 6]
  8: [1, 3]
  9: [2, 4]
}

numStringsEndingIn = {
    0: 2,
    1: 2,
    ...
    6: 3,
    ...
}

i = 3:


nextNumStringsEndingIn = {
    0: ,
    1: ,
    ...
    4: 2,
    ...
    6: 2,
    ...
}



def knightDialer(n):
    possibleJumps = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    
    3^n
    
    10*n
    
    dp
    the solution for "calculateTotal"
    for each of the 10 numbers
    at each remaining depth from 0 to n
		
		dp [
    	[-1,-1,-1, ...] (of length n)
      [-1,-1,-1, ...]
      ...
      [-1,-1,-1, ...]
    ]
    
    initially dp[number][remainingdepth] = -1
    
    calculateTotal(remainingDepth, number)
    --> dp[number][remainingdepth] = calculateTotal(remainingDepth, number)
    
    

    numStringsEndingIn = {
        0: 1,
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
        8: 1,
        9: 1,
    }

    for i in range(2, n + 1):
        nextNumStringsEndingIn = collections.defaultdict(self.defaultValue)
        for key, val in numStringsEndingIn.items():
            for possibleJump in possibleJumps[key]:
                nextNumStringsEndingIn[possibleJump] += val
        numStringsEndingIn = nextNumStringsEndingIn

    finalCount = 0
    for stringCountEndingInValue in numStringsEndingIn.values():
        finalCount += stringCountEndingInValue

    return finalCount % (10**9 + 7)
   
# USE "defaultdict" with a function
# @lru_cache??
# 















