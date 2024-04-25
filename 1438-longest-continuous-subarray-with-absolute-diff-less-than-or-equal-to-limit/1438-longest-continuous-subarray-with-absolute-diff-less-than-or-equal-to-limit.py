class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        min_deque = deque()
        max_deque = deque()
        l = 0
        max_len = 0
        
        for r in range(len(nums)):
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()
                
            min_deque.append(r)
            max_deque.append(r)
            
            while abs(nums[max_deque[0]]-nums[min_deque[0]]) > k:
                if min_deque[0] == l:
                    min_deque.popleft()
                if max_deque[0] == l:
                    max_deque.popleft()
                l += 1
                
            max_len = max(max_len, r-l+1)
            
        return max_len