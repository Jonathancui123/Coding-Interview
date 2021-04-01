'''
O(n) time and O(n) space Use a set -> 
O(nlogn) time O(1) space --> sort it in place
O(n) time O(1) space (Modified) Cyclic sort --> Regular cyclic sort except the second instasnce of the duplicated number will be deposited at the origin of it's cycle
ANOTHER SOLUTION: [Negative at index for marker]
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        