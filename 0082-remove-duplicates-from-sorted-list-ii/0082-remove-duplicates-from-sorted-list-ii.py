# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        answer = dummy

        import collections
        counter = collections.defaultdict(int)

        while head:
            counter[head.val] += 1
            head = head.next

        for val in counter:
            if counter[val] <= 1:
                next_node = ListNode(val, None)
                dummy.next = next_node
                dummy = dummy.next

        return answer.next
                
        
            