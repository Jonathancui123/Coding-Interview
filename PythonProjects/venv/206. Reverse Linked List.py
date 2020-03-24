# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Base case and build:
# On each step we want to reach forward and make the next node point to the current
# 1. No next node: Empty list, last nnode in list. Return current node. 
# 2. There exists a next node:
# - Call the function on the next node so that everything beyond is reversed --> Save the return value
# - Make the next node point to current node
# - Pass up the return value



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        else:
            temp = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return temp
    