# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = float("inf")
    prev = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.answer

    def inorder(self, node):
        # inorder traversal
        if node is None:
            return

        self.inorder(node.left)

        if self.prev is not None:
             self.answer = min(self.answer, node.val - self.prev.val)
        self.prev = node

        self.inorder(node.right)

        
