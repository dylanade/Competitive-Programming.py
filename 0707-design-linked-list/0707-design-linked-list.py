class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
class MyLinkedList:  
    def __init__(self):
        self.head = Node(0)
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        current = self.head
        for _ in range(index+1): current = current.next
        return current.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return
        current = self.head
        for _ in range(index): current = current.next
        new_node = Node(val, current.next)
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        current = self.head
        for _ in range(index): current = current.next
        current.next = (current.next).next
        self.size -= 1  


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)