# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        
        if head is None:
            return None
#         need a first point
        first = None
#         need a second point
        second = head
#     third point 
        third = head.next
        
        while second:
            second.next = first
            first = second
            second = third
            if third is not None:
                third = third.next
        return first
        