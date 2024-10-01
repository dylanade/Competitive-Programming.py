class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        answer = 0
        for i in range(len(nums)-1, -1, -1):
            r = bisect_right(nums, upper - nums[i], 0, i)
            l = bisect_left(nums, lower - nums[i], 0, i)
            answer += (r - l)
        return answer 