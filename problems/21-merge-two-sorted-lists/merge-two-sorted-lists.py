# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val < list2.val:
                head = list1
                left_node = list1.next
                right_node = list2
            else:
                head = list2
                left_node = list1
                right_node = list2.next

            tail = head
        
            while left_node is not None and right_node is not None:
                if left_node.val < right_node.val:
                    tail.next = left_node
                    tail = left_node
                    left_node = left_node.next
                else:
                    tail.next = right_node
                    tail = right_node
                    right_node = right_node.next

            if left_node is not None:
                while left_node is not None:
                    tail.next = left_node
                    tail = left_node
                    left_node = left_node.next
            
            if right_node is not None:
                while right_node is not None:
                    tail.next = right_node
                    tail = right_node
                    right_node = right_node.next

            return head

        else:
            if list1:
                return list1
            elif list2:
                return list2
            else:
                return None
