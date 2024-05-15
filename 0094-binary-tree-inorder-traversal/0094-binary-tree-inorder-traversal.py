# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        def traverse(root):
            if(root):
                traverse(root.left)
                self.answer.append(root.val)
                traverse(root.right)
        traverse(root)
        return self.answer

        