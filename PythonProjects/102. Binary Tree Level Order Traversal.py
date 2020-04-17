# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preOrder(self, root, depth, storage):
        if (root == None):
            return
        if (len(storage) <= depth):
            storage.append([])
        storage[depth].append(root.val)
        self.preOrder(root.left, depth + 1, storage)
        self.preOrder(root.right, depth + 1, storage)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        storage = []
        self.preOrder(root, 0, storage)
        return storage
        