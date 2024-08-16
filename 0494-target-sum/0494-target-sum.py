class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for each num: can add or subtract
        # states: index, total (is_total == target)

        dp = {} # (ndex, total) = # of ways to get to target

        def bt(i, total):
            if i == len(nums):
                return 1 if total == target else 0 # (there is a way)
            
            if (i, total) in dp:
                return dp[(i, total)]

            yadd = bt(i + 1, total + nums[i])
            nadd = bt(i + 1, total - nums[i])
            dp[(i, total)] = yadd + nadd
            return dp[(i, total)]

        return bt(0, 0)

