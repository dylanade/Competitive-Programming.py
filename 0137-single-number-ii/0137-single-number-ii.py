class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        import collections
        count = collections.Counter(nums)
        for num in count:
            if count[num] == 1:
                return num
        return -1