# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        left = l1
        right = l2

        head = None
        tail = None
        carry = 0
        while left or right:
            left_value = left.val if left else 0
            right_value = right.val if right else 0
            cal = left_value + right_value + carry
            carry = 1 if cal > 9 else 0
            cur_value = cal % 10
            cur_node = ListNode(cur_value)

            if head is None:
                head = cur_node
                tail = cur_node
            else:
                tail.next = cur_node
                tail = tail.next

            if left:
                left = left.next
            if right:
                right = right.next
        
        if carry:
            tail.next = ListNode(1)
            tail = tail.next

        return head