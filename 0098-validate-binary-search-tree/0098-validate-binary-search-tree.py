# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS: O(n)
        # BRUTE FORCE check every subtree value and root: O(n) -> O(n^2)

        def valid(node, left, right): # left and right boundary
            if not node:
                return True # Empty BST is still a BST
            
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))

        


        