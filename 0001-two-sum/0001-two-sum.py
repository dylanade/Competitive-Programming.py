class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, num in enumerate(nums):
            if target-num not in prev:
                prev[num] = i
            else:
                return [prev[target-num], i]

        return []
