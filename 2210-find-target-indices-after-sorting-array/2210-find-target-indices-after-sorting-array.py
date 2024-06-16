class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i, num in enumerate(sorted(nums)):
            if num == target:
                indices.append(i)
        return indices
        