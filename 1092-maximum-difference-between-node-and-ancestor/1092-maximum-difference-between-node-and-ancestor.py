# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #DFS
        max_val = 0
        q = deque([(root, root.val, root.val)])

        while q:
            cur, high, low = q.popleft()
            cur_val = cur.val
            max_val = max(max_val, cur_val-low, high-cur_val)

            if cur.left:
                q.append((cur.left, max(cur_val, high), min(cur_val, low)))

            if cur.right:
                q.append((cur.right, max(cur_val, high), min(cur_val, low)))
        
        return max_val

        