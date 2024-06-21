# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, array):
        if root != None:
            self.inorder(root.left, array)
            array.append(root.val)
            self.inorder(root.right, array)

    def buildTree(self,array,low,high):
        if low > high:
            return None
        mid = (low + high)//2
        root = TreeNode(array[mid])
        root.left = self.buildTree(array, low, mid-1)
        root.right = self.buildTree(array, mid+1, high)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = []
        self.inorder(root, array)
        low = 0
        high = len(array) - 1
        root = self.buildTree(array, low, high)
        return root

        
        