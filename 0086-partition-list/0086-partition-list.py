# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1 = ListNode(0)
        list2 = ListNode(0)
        
        current = head
        l1 = list1
        l2 = list2
        while current:
            if current.val < x:
                list1.next = current
                list1 = list1.next
            else:
                list2.next = current
                list2 = list2.next
            
            temp = current.next
            current.next = None
            current = temp

        print(l1)
        print(l2)
        list1.next = l2.next
        return l1.next
        
# if cur.val < x:
# list1.next = current
# temp = current.next
# cur.next =None
# cur = temp
    
        
        