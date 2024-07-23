# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = queue.Queue()
        q.put((root, 1))
        max_step = 0
        while q.qsize():
            cur, cur_step = q.get()
            if cur is None:
                continue
            max_step = max(max_step, cur_step)
            if cur.left:
                q.put((cur.left, cur_step + 1))
            if cur.right:
                q.put((cur.right, cur_step + 1))
        
        return max_step