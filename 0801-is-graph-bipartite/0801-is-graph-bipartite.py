class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # splitting graph into two sets
        # every vertex cannot be in the same set as it's neighbours
        # check if there is an odd cycle -> NOT bipartite
        
        n = len(graph)
        colours = [0] * n # map node i
        # red = 1 
        # blue = -1

        def dfs(i):
            if colours[i]:
                return True
                
            q = deque([i])
            colours[i] = 1

            while q:
                i = q.popleft()
                for a in graph[i]:
                    # adjacent node is same colour (NOT bipartite)
                    if colours[a] == colours[i]:
                        return False
                    elif colours[a] == 0:
                        colours[a] = -colours[i]
                        q.append(a)
            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True