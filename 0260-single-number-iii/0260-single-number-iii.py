class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        import collections
        count = collections.Counter(nums)
        ans = []
        for num in count:
            if count[num] == 1:
                ans.append(num)
        return ans
