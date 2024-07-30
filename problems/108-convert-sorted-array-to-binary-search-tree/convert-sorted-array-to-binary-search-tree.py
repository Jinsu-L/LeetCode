# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # height-balanced binary search tree로 만들어라???
        # 반잘라서.. left랑 right tree를 만든다.. 그리고 mid로 연결한다..
        nums_size = len(nums)
        if nums_size == 0:
            return None
        mid = nums_size // 2
        print(nums_size,mid, mid+1)
        left_tree = self.sortedArrayToBST(nums[:mid])
        right_tree = self.sortedArrayToBST(nums[mid+1:])
        current_node = TreeNode(nums[mid], left_tree, right_tree)

        return current_node