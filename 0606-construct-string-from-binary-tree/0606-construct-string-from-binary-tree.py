# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # preorder traversal
        answer = [] # str("") | adding strings together is not efficient

        def preorder(node):
            if not node:
                return 
            
            answer.append("(")
            answer.append(str(node.val))

            if not node.left and node.right:
                answer.append("()")

            preorder(node.left)
            preorder(node.right)

            answer.append(")")
            
            return "".join(answer[1:-1])

        return preorder(root)