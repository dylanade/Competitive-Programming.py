class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        answer = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    answer += 1

        return answer