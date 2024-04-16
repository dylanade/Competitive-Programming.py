# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = None
        current = head
        
        while current:
            next_node = current.next
            current.next = reversed_list
            reversed_list = current
            current = next_node
    
        return reversed_list
        
            
        