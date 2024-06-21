class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], q: List[List[str]]) -> List[float]:
        # observations:
        # can not determine each individual value due to ambiguity
        # there is too many answers for each value (can not explicitly solve for x)
        # find the equation: a/b * b/x, where we can eliminate denominators
        # can find the inverses of each equation: a/b = x, b/a = 1/x

        graph = collections.defaultdict(list)

        for i, (x, y) in enumerate(e):
            graph[x].append((y, v[i])) # (vertex, edge weight)
            graph[y].append((x, 1/v[i])) 

        def dfs(x, y):
            if x not in graph or y not in graph:
                return -1

            queue = deque()
            queue.append([x, 1])

            visited = set() 
            visited.add(x)

            while queue:
                a, value = queue.pop()

                if a == y:
                    return value

                for neighbour, weight in graph[a]:
                    if neighbour not in visited:
                        queue.append([neighbour, value * weight])
                        visited.add(neighbour)
                
            return -1 # no path connnecting x, y

        answer = [-1] * len(q)
        for i, query in enumerate(q):
            answer[i] = dfs(query[0], query[1])

        return answer