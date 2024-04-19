# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = defaultdict(int)
        
        while head:
            count[head.val] += 1
            head = head.next
            
        
        head = None
        prev = None
        for value in sorted(count.keys(), reverse=True):
            if count.get(value) == 1:
                head = ListNode(value, prev)
                prev = head
          
        return head
        