# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        q = deque([(root, root.val)])

        while q:
            cur_node, cur_sum = q.popleft()

            if cur_node.left is None and cur_node.right is None and cur_sum == targetSum:
                return True
            if cur_node.left is not None:
                q.append((cur_node.left, cur_sum + cur_node.left.val))
            if cur_node.right is not None:
                q.append((cur_node.right, cur_sum + cur_node.right.val))

        return False