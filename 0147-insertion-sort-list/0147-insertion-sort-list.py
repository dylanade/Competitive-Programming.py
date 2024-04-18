# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def insertion_sort(input_list):
#     for index in range(1, len(input_list)):
#         current_value = input_list[index]
#         position = index
#         while position > 0 and input_list[position - 1] > current_value:
#             input_list[position] = input_list[position - 1]
#             position -= 1
#         input_list[position] = current_value
#     return input_list


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = head
        curr = head.next
        
        while curr:
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue

            temp = dummy
            while curr.val > temp.next.val:
                temp = temp.next

            prev.next = curr.next
            curr.next = temp.next
            temp.next = curr
            curr = prev.next

        return dummy.next
        
        
        
            
            
        
        