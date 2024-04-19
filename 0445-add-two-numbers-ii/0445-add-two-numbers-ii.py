# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_str = ''
        l2_str = ''
        
        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
            
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next
            
        total = str(int(l1_str) + int(l2_str))
    
        head = ListNode()
        current = head
        for value in total:
            current.next = ListNode(value)
            current = current.next
            
        return head.next
        