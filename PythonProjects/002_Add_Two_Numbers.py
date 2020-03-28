# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 
# 
# 

class Solution:
    def addHelper(self, l1, l2, carry):
        if (l1 == None and l2 == None and carry == 0):
            return None
        result = 0        
        if (l1 != None):
            result += l1.val
        if (l2 != None):
            result += l2.val
        result += carry
    
        newNode = ListNode()
        newNode.val = result % 10
        newNode.next = self.addHelper(None if l1 == None else l1.next , None if l2 == None else l2.next, result // 10)
        return newNode
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addHelper(l1, l2, 0)