class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current |= nums[j]
                if current >= k: 
                    ans = min(ans, j-i+1)
        return -1 if ans==float('inf') else ans