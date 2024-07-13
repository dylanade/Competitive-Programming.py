class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = collections.deque([n-1])

        for i in range(n-2, -1, -1):
            if queue[0] - i > k:
                queue.popleft()
            nums[i] += nums[queue[0]]
            while len(queue) and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)

        return nums[0]