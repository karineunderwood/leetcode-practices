# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
         # create an empty, "moving" head
        head = ListNode()
        # create another, "standing" head, that will be returned in the end
        result = head
        # while both lists are "alive":
        while list1 and list2:
             # check if list1-valalue is lower than list2.value
            if list1.val < list2.val:
                # setting head.next
                # move on
                head.next = list1
                head = list1
                list1 = list1.next
            # same "elsewise" actions
            else:
                head.next = list2
                head = list2
                list2 = list2.next
                
            if list1:
                head.next = list1
            if list2:
                head.next = list2
        return result.next
                
            
                      
            
                      
                 
                
                   
        
           
                
        