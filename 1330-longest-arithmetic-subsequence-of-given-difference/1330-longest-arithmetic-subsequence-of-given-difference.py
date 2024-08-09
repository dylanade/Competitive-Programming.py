class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # bottom up
        # dp = {}
        # max_length = 0

        # for n in arr:
        #     if n - difference in dp:
        #         dp[n] = dp[n - difference] + 1
        #     else:
        #         dp[n] = 1
            
        #     max_length = max(max_length, dp[n])
        
        # return max_length

        @lru_cache(None)
        def dp(i):
            # check if the next element in the sequence exists
            next_val = arr[i] + difference
            if next_val in value_to_index:
                # find the index of next_val that is greater than i
                for j in value_to_index[next_val]:
                    if j > i:
                        return 1 + dp(j)
            return 1

        # dictionary to store indices of each value
        value_to_index = {}
        for i, v in enumerate(arr):
            if v not in value_to_index:
                value_to_index[v] = []
            value_to_index[v].append(i)

        # compute the longest subsequence
        max_length = 0
        for i in range(len(arr)):
            max_length = max(max_length, dp(i))
        
        return max_length