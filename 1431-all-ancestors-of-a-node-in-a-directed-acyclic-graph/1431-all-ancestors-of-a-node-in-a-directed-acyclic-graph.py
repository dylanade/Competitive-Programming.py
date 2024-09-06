class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegrees = [0] * n
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            indegrees[v] += 1

        result = [set() for _ in range(n)]

        queue = deque()
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                result[neighbor].update(result[node], [node])
                indegrees[neighbor] -= 1

                if not indegrees[neighbor]:
                    queue.append(neighbor)

            result[node] = sorted(result[node])
            
        return result