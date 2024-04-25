class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        max_queue = deque()  # store maximum values
        min_queue = deque()  # store minimum values
        l = 0

        for num in nums:
            # Maintain the max_queue in decreasing order of elements
            while max_queue and num > max_queue[-1]:
                max_queue.pop()
            max_queue.append(num)

            # Maintain the min_queue in increasing order of elements
            while min_queue and num < min_queue[-1]:
                min_queue.pop()
            min_queue.append(num)

            # If the absolute difference between the maximum and minimum elements
            # in the current window exceeds the limit, remove one element
            # from either or both queues and increment the left pointer
            if max_queue[0] - min_queue[0] > k:
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
                if min_queue[0] == nums[l]:
                    min_queue.popleft()
                l += 1

        return len(nums) - l 