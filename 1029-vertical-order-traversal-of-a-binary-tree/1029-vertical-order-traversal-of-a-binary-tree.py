# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS + Sorting
        # moving left (row + 1, col - 1)
        # moving right (row + 1, col + 1)
        # using map to store {col: [nodes]}
        # sort nodes 

        if not root:
            return []

        columns = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)]) # node, row, col
        min_col = float("inf")
        max_col = float("-inf")

        while queue:
            node, row, col = queue.popleft()

            if col < min_col:
                min_col = col
            
            if col > max_col:
                max_col = col

            # keeping track of rows for row order
            columns[col].append((node.val, row))

            if node.left:
                queue.append((node.left, row+1, col-1))

            if node.right:
                queue.append((node.right, row+1, col+1))

        answer = []

        for column in range(min_col, max_col+1):
            items = columns[column]
            # sort by row then by column
            items.sort(key=lambda x:(x[1], x[0]))
            items = [col for col, _ in items]
            answer.append(items)

        return answer