# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        def dfs(node, path, target):
            if not node:
                return "" # Evaluates to False in Python

            if node.val == target:
                return path

            path.append("L")
            result = dfs(node.left, path, target)
            if result:
                return result

            path.pop()
            path.append("R")
            result = dfs(node.right, path, target)
            if result:
                return result

            path.pop()
            return ""

        start_path = dfs(root, [], start)
        end_path = dfs(root, [], end)
        i = 0

        while i < min(len(start_path), len(end_path)):
            if start_path[i] != end_path[i]:
                break
            i += 1

        result = ["U"] * len(start_path[i:]) + end_path[i:]    
        return "".join(result)