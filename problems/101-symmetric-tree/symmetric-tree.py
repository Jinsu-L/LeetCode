# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkSubTree(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return left.val == right.val and self.checkSubTree(left.left, right.right) and self.checkSubTree(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSubTree(root, root)