class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # DAG (directed acyclic graph) is a tree
        parent = [False] * n
        for u, v in edges:
             parent[v] = True

        answer = []
        for u in range(n):
            if not parent[u]:
                answer.append(u)

        return answer