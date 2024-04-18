# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 0
        while current:
            current = current.next
            size += 1
        node_at = size-n-1
        if node_at < 0:
            head = head.next
            return head
        current = head
        for i in range(node_at):
            current = current.next
        current.next = current.next.next
        return head
    
#         temp = ListNode(0,head)
#         left = temp
#         right = head

#         while n > 0 and right:
#             right = right.next
#             n -= 1
        
#         while right:
#             left = left.next
#             right = right.next
#         left.next = left.next.next

#         return temp.next
