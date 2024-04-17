# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        startNode = ListNode()
        leftNode = head
        i = 1
        while i < left:
            startNode = leftNode
            leftNode = leftNode.next
            i += 1

        rightNode = leftNode
        i = left
        
        while i < right:
            rightNode = rightNode.next
            i += 1
        
        for i in range(right - left):       
            temp = leftNode.next
            leftNode.next = rightNode.next
            rightNode.next = leftNode
            startNode.next = temp
            leftNode = temp

        if left == 1:
            head = startNode.next
            
        return head
            
            