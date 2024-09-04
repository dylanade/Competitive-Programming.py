# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        curr = head

        while curr and curr.next:
            temp = curr.next.next

            tail.next = curr.next
            curr.next.next = curr
            curr.next = temp

            tail = curr
            curr = temp

        return dummy.next