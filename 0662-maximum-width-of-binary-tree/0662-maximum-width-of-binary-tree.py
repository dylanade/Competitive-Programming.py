# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        q = deque([[root, 1, 0]]) # root, index, level
        prev_level, prev_index = 0, 1 
        #prev_index init 1 because of edge case root = [1]
        #prev_index is just the first node index of that level
        while q:
            node, index, level = q.popleft()

            if level > prev_level:
                prev_level = level
                prev_index = index
            
            answer = max(answer, index - prev_index + 1)

            if node.left:
                q.append([node.left, 2*index, level+1])

            if node.right:
                q.append([node.right, 2*index+1, level+1])

        return answer    


        