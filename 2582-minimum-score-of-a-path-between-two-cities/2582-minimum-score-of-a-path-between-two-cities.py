class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # path from 1 to n
        # minimal edge in a connected component

        # O (E + V) -> BFS/DFS 

        graph = collections.defaultdict(list) # weighted graph (neighbour, distance)

        for u, v, d in roads: # source, destination, distance
            graph[u].append((v, d))
            graph[v].append((u, d))

        answer = float("inf") # minimisation

        queue = collections.deque()
        queue.append((1))

        visited = set()

        while queue:
            node = queue.popleft()

            if node in visited:
                continue
        
            for neighbour, distance in graph[node]:
                if neighbour not in visited:
                    answer = min(answer, distance)
                    queue.append((neighbour))

            visited.add(node)

        return answer

        