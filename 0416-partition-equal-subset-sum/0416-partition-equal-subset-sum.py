class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # two choices: skip or don't skip a number
        # states: target and index
        sum_nums = sum(nums)

        if sum_nums % 2 == 1:
            return False

        target = sum_nums // 2

        dp = [False] * (target + 1)
        dp[0] = True  

        for num in nums:
            for curr in range(target, num-1, -1):  # avoid going out-of-bounds
                if dp[curr-num]:
                    dp[curr] = True

        return dp[target]  