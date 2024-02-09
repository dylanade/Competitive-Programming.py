class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        position = {num: i for i, num in enumerate(nums)}
        for i, j in operations:
            nums[position[i]] = j
            position[j] = position[i]
            del position[i]
        
        return nums