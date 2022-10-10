# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         get the length of the LL
        list_length = 0
        current = head
        node = head
        counter = 0
        
        while current:
            list_length += 1
            current = current.next
            
        middle = list_length // 2
        
        while node:
            if counter == middle:
                return node
            else:
                counter += 1
                node = node.next
        return None
        
        
        
        
    
            
        
        