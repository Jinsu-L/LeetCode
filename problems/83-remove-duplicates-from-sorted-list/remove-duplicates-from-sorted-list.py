# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        visited = set()
        while cur is not None:
            if cur.val in visited:
                prev.next = cur.next
                cur = cur.next
            else:
                visited.add(cur.val)
                prev = cur
                cur = cur.next
        
        return head
