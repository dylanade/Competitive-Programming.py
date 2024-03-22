class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        add = 0;
        ans = 0;
        mp = {}
        mp[0] = 1
        
        for num in nums:
            add += num
            if (add-k) in mp.keys():
                ans += mp.get(add-k)
            mp[add] = mp.get(add, 0) + 1
        
        return ans
        
# Intuition
# The problem requires us to find the number of subarrays that satisfies the condition.

# Approach
# Hash + Prefix Sum,
# So, the problem converts to that whether we can find the difference in the map, we go through the array and use a hashmap to store prefix sum(key) and its count of index(value), and update current prefix sum into map. Finally, if we find it, use a variable to sum up the result.

# Complexity
# Time complexity:
# O(n), only traverse array once.

# Space complexity:
# O(n)