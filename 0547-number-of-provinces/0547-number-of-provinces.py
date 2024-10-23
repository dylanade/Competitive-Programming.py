class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor, connected in enumerate(isConnected[city]):
                if connected == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        n_provinces = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                visited.add(city)
                dfs(city)
                n_provinces += 1

        return n_provinces