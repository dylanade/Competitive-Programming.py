class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # What makes a binary tree valid?
            # connected
            # no cycle

        # Problems:
            # trees are undirected graph
            # if two nodes connected to one child node then:
                # a cycle -> INVALID BT

        hasParent = set(leftChild + rightChild)  # unique children
        hasParent.discard(-1) # discard safer than remove

        if len(hasParent) == n: # no root node
            return False

        root = -1

        for i in range(n):
            if i not in hasParent:
                root = i
                break
        
        visited = set()

        def dfs(i):

            if i == -1:
                return True

            if i in visited:
                return False

            visited.add((i))
            return dfs(leftChild[i]) and dfs(rightChild[i])

        return dfs(root) and len(visited) == n
        