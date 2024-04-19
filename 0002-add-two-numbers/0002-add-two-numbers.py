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
            
        num1 = l1_str[::-1]
        num2 = l2_str[::-1]
        total = str(int(num1) + int(num2))
        
        head = None
        prev = None
        for i in range(len(total)):
            head = ListNode(total[i], prev)
            prev = head
        return head
        
        
            
        
            
        
            