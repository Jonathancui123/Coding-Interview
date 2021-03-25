# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# NOTE: Don't use In-order traversal --> they don't guarantee same structure



# Attempt 1:
# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if (s == None):
#             return False
#         if (s.val == t.val):  # NO NEED TO CHECK FOR EQUALITY 
#             if (self.subtreeMatch(s, t)):
#                 return True
        
#         leftMatch = self.isSubtree(s.left, t)
#         rightMatch = self.isSubtree(s.right, t)
#         return leftMatch or rightMatch
            
#     def subtreeMatch(self, s: TreeNode, t: TreeNode) -> bool:
#         if (s == None and t == None):
#             return True
#         if (s!= None and t != None and s.val == t.val):
#             leftMatch = self.subtreeMatch(s.left, t.left)
#             rightMatch = self.subtreeMatch(s.right, t.right)
#             return leftMatch and rightMatch
#         return False

  
# Attempt 2:
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if (s == None):
            return False
        if (self.subtreeMatch(s, t)):
            return True
        
        leftMatch = self.isSubtree(s.left, t)
        rightMatch = self.isSubtree(s.right, t)
        return leftMatch or rightMatch
            
    def subtreeMatch(self, s: TreeNode, t: TreeNode) -> bool:
        if (s == None and t == None):
            return True
        elif (s == None or t == None):
            return False
        if (s.val == t.val):
            leftMatch = self.subtreeMatch(s.left, t.left)
            rightMatch = self.subtreeMatch(s.right, t.right)
            return leftMatch and rightMatch
        return False


# 
# # O(m*n)
# Will in-order traversal work for finding matching "structure and node values"
# No it will not:
#         b
#        / \
#       a   c  
    
#         c
#        / 
#       a   
#        \
#         b