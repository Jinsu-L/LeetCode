# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    sums = defaultdict(list)

    def travelOfNodes(self, root: Optional[TreeNode], level=0):
        if root is None:
            return 

        self.sums[level].append(root.val)
        self.travelOfNodes(root.left, level + 1)
        self.travelOfNodes(root.right, level + 1)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.sums = defaultdict(list)
        self.travelOfNodes(root, 0)
        return [ sum(self.sums[i]) / len(self.sums[i]) for i in range(len(self.sums))]
            




