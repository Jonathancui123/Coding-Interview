# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = deque()

        if (root == None):
            return
        #Visit root node
        prev = root
        if (None != root.right):
            stack.append(root.right)
        if (None != root.left):
            stack.append(root.left)
        root.left = None
        
        while(len(stack) > 0):
            curr = stack.pop()
            prev.right = curr
            if (None != curr.right):
                stack.append(curr.right)
            if (None != curr.left):
                stack.append(curr.left)
            curr.left = None
            prev = curr
        
            

        
        
        