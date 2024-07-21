# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        tail = head.next
        while tail is not None:
            middle = middle.next
            tail = tail.next
            if tail:
                tail = tail.next

        return middle