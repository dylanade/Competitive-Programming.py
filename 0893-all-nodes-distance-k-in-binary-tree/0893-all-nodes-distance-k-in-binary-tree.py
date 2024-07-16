# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]

        graph = collections.defaultdict(list)

        queue = collections.deque()
        queue.append((root))

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
            
        answer = []

        queue = collections.deque() # node, distance
        queue.append((target, 0))

        visited = set()
        visited.add((target))

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                answer.append(node.val)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append((neighbour, distance + 1))
                    visited.add(neighbour)

        return answer
        