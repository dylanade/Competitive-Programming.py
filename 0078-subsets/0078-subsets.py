from itertools import chain, combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

        # # 2^n = number of subsets
        # # Worst Case: O(n * 2^n)

        # answer = []
        # subset = []

        # def dfs(i): # backtracking using dfs
        #     # base cases
        #     if i >= len(nums):
        #         answer.append(subset[:])
        #         return

        #     # decisions
        #     # decision to include nums[i]
        #     subset.append(nums[i])
        #     dfs(i + 1)

        #     # decision NOT to include nums[i]
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return answer

        return powerset(nums)