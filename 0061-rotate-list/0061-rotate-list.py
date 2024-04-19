# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head

        tail = head
        l = 1 #length
        while tail.next:
            tail = tail.next
            l += 1
        tail.next = head

        m = l-(k%l)
        while m > 0:
            head = head.next
            tail = tail.next
            m -= 1

        tail.next = None
        return head