# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
    
        current = head
        count = 1
        while current:
            current = current.next
            count += 1
            
        mid_node = head
        mid = count/2
        while mid > 1:
            mid_node = mid_node.next
            mid -= 1
        
        return mid_node