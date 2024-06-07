class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # TLE: 79/80 TC Passed
        # for (x, y) in operations:
        #     i = nums.index(x)
        #     nums[i] = y
        # return nums

        position = {num:i for i, num in enumerate(nums)}
        for i, j in operations:
            nums[position[i]] = j
            position[j] = position[i]
            del position[i]
        
        return nums