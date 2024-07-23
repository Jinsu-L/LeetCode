# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def get_nodes(self, root):
        if root is None:
            return [None]
        return [root.val] + self.get_nodes(root.left) + self.get_nodes(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.get_nodes(p) == self.get_nodes(q)
            
