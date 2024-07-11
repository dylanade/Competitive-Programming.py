class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = collections.deque()
        queue.append((0))

        visited = [False] * len(rooms)
        visited[0] = True

        while queue:
            current_key = queue.popleft()

            for key in rooms[current_key]:
                if not visited[key]:
                    queue.append((key))
                    visited[key] = True

        for visit in visited:
            if not visit:
                return False

        return True
        


        