class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = []

        for cost in costs:
            a, b = cost
            differences.append((a, b, b-a))

        differences = sorted(differences, key=lambda city: city[2])
        n = len(costs)
        total = 0

        for i in range(n // 2):
            total += differences[i][1]

        for i in range(n // 2, n):
            total += differences[i][0]

        return total
