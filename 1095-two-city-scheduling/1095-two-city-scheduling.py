class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        differences = []
        for i in range(n):
            a, b = costs[i]
            differences.append((a-b, a, b)) # difference, aCost, bCost

        differences.sort()
        total = 0

        for i in range(n // 2):
            total += differences[i][1]

        for i in range(n // 2, n):
            total += differences[i][2]

        return total