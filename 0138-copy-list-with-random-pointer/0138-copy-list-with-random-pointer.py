"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}
        
        current = head
        while current:
            new_node = Node(current.val)
            hashmap[current] = new_node
            current = current.next
            
        current = head
        while current:
            copy = hashmap[current]
            copy.next = hashmap[current.next]
            copy.random = hashmap[current.random]
            current = current.next
        
        return hashmap[head]
        
            
        

            
        