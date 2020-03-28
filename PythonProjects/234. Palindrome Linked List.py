# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class NodeBool:
    def __init__(self, Node: ListNode, isPal: bool):
        self.Node = Node
        self.isPal = isPal

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Reduce the list on both sides until you get to the middle (base case)
        # But retain access to the remaining end of the list
        length = 0
        temp = head
        while (temp != None):
            length += 1
            temp = temp.next
        retNodeBool = self.isPalHelper(head, length)
        return retNodeBool.isPal
        
    def isPalHelper(self, head: ListNode, length: int):
        # Middle node base case: Length is 0 or 1
        if length == 0:
            return NodeBool(head, True)
        if length == 1:
            return NodeBool(head.next, True)
        retNodeBool = self.isPalHelper(head.next, length-2)
        isPal = (head.val == retNodeBool.Node.val) and retNodeBool.isPal
        return NodeBool(retNodeBool.Node.next, isPal)