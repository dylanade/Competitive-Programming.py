# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        # The value that every node needs to have to make the tree univalued
        val = root.val
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Go over all the nodes in current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If the node does not have same value as "val",
                if node.val != val: 
                    return False
                
                # Push the left child
                if node.left: 
                    queue.append(node.left)
                
                # Push the right child
                if node.right: 
                    queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1

        # The tree is univalued
        return True