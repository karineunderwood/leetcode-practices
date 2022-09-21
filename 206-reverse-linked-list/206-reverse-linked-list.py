# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        

#         start with two pointer current and prev. Current set to the head and prev set to none

#    have a third node pointing to the current.next 
        current = head
        prev = None
        
        while current:
            third_node = current.next
            current.next = prev
            prev = current
            current = third_node
        return prev