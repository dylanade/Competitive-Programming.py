import math
import collections

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = collections.defaultdict(set)
        
        for i in range(n):  # i is the source
            for j in range(n):
                if i == j:
                    continue

                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:  # reachable from i
                    graph[i].add(j)

        # return None
        def dfs(bomb, seen):  
            if bomb in seen:
                return

            seen.add(bomb)
            for neighbour in graph[bomb]:
                dfs(neighbour, seen)

        answer = 0
        for i in range(n):
            seen = set()
            dfs(i, seen)
            answer = max(answer, len(seen))

        return answer
        
        # # observations
        # # calculate the euclidean distance of bombs between each other
        # # BRUTE FORCE: O(n^2)

        # answer = 0
        # count = collections.defaultdict(int)

        # for i, bomb in enumerate(bombs):
        #     bombs[i] = tuple(bomb)
        #     count[bombs[i]] += 1

        # print(count)

        # for i in range(len(bombs)):
        #     for j in range(len(bombs)):
        #         x1, y1, r1 = bombs[i]
        #         x2, y2, r2 = bombs[j]

        #         if count[bombs[j]]:
        #             count[bombs[j]] -= 1
        #             distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #             if distance <= (r1 + r2):
        #                 answer += 1

        # return answer