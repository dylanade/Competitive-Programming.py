# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(height, node):
                if node:
                    if node.left and node.right:
                        height_left = traverse(height, node.left)
                        height_right = traverse(height, node.right)
                        height += max(height_left, height_right)
                    elif node.left:
                        height += traverse(height, node.left)
                    elif node.right:
                        height += traverse(height, node.right)
                return height
        if root:
            return traverse(1, root)
        else:
            return 0
        