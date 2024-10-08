class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        MOD = 10**9 + 7
        ans = SortedList()
        count = 0
        
        for i in instructions:
            less = ans.bisect_left(i)
            more = len(ans) - ans.bisect_right(i)
            ans.add(i)
            count += min(less, more)
        
        return count % MOD