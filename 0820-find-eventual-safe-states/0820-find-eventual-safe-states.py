class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        n = len(graph)
        
        def dfs(node):
            if not node in safe:
                safe[node] = False
                for neighbor in graph[node]:
                    if not dfs(neighbor): break
                else: safe[node] = True
            return safe[node]
        
        answer = []

        for i in range(n):
            if dfs(i):
                answer.append(i)

        return answer