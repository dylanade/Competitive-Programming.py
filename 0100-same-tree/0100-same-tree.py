# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # using DFS - Depth First Search
        if not p and not q: #both trees is empty
            return True
        if not p or not q or (p.val != q.val): #one tree is empty
            return False
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))