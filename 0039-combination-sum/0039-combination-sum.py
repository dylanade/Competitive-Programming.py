class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, current, total): # current = current combination, total = sum
            # base cases
            # reached goal
            if total == target:
                answer.append(current.copy())
                return

            # cannot reach goal
            if i >= len(candidates) or total > target:
                return

            # decisions
            # want to add candidate to combination
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])

            # removing candidate
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return answer