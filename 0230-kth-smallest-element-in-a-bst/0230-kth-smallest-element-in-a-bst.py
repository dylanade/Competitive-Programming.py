# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST 
        # put the elements in sorted order and return sorted_arr[k-1]
        # n = 0
        # cur = root
        # stack = []

        # while cur and stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
            
        #     cur = stack.pop() # popping most recent value added
        #     n += 1
        #     if n == k:
        #         return int(cur.val) if (cur) else 0
        #     cur = cur.right

        # iterative solution
        res = []

        def inorder(node): #LNR
            if not node:
                return
            inorder(node.left)
            if len(res) == k:
                return
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[-1]