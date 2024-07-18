class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = []

        for cost in costs:
            a, b = cost
            differences.append((a-b, a, b)) # city[0], city[1], city[2]

        differences = sorted(differences)
        n = len(costs)
        total = 0

        # process a in first half 
        for i in range(n // 2):
            total += differences[i][1]

        # process b in second half 
        for i in range(n // 2, n):
            total += differences[i][2]

        return total