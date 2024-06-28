class Solution:
    def shortestAlternatingPaths(self, n: int, r: List[List[int]], b: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for u, v in r:
            red[u].append(v)

        for u, v in b:
            blue[u].append(v)

        answer = [-1 for _ in range(n)]
        # answer[0] = 0 # base case, knowing first gonna always be 0

        queue = collections.deque()
        queue.append([0, 0, None]) # [node, length, prev_edge_color]

        visited = set()
        visited.add((0, None))

        while queue:
            node, length, edge_color = queue.popleft()

            if answer[node] == -1:
                answer[node] = length

            if edge_color != "RED": # BLUE
                for neighbour in red[node]:
                    if (neighbour, "RED") not in visited:
                        visited.add((neighbour, "RED"))
                        queue.append([neighbour, length + 1, "RED"])
            
            if edge_color != "BLUE": # RED
                for neighbour in blue[node]:
                    if (neighbour, "BLUE") not in visited:
                        visited.add((neighbour, "BLUE"))
                        queue.append([neighbour, length + 1, "BLUE"])

        return answer
                
            
            


        