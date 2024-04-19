# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = []
        
        while head:
            if head.val not in check:
                check.append(head.val)
            head = head.next
        
        head = None
        prev = None
        for value in check[::-1]:
            head = ListNode(value, prev)
            prev = head
        
        return head