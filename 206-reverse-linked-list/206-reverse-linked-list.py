# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        

# TWO POINTER APPROACH
# HAVE A POINTER POINTING TO THE HEAD
# HAVE A PREVIOUS POINTER POINTING TO NULL
# WHILE THE HEAD IS NOT NULL:
#   SET CURRENT.NEXT = NULL
#   SET PREVIOUS TO CURRENT
#   SET CURRENT TO NEXT POINTER

        prev = None
        current = head
        
        while current:
            next_pointer = current.next
            current.next = prev
            prev = current
            current = next_pointer
        return prev
        