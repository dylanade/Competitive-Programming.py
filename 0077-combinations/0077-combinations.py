class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n = 4 -> 1, 2, 3, 4
        # k = 2 -> Decision Tree
        answer = []
        combination = []

        def backtrack(start):
            # base cases
            if len(combination) == k:
                answer.append(combination[:])
                return
            
            # decisions
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1)
                combination.pop()

        backtrack(1)
        return answer