class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_unique = set(nums)
        return len(set_unique) != len(nums)