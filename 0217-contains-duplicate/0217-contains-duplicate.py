class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        for key in count:
            if count[key] >= 2:
                return True
        return False