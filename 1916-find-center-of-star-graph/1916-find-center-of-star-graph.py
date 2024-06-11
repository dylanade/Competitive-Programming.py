class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u, v = edges[0][0], edges[0][1]
        count_u, count_v = 0, 0

        for edge in edges:
            if u in edge: count_u += 1
            if v in edge: count_v += 1

        return u if count_u == len(edges) else v