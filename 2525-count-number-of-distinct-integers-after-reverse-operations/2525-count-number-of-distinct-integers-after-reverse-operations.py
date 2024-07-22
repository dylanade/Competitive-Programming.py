class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique = set(nums)
        for num in nums:
            unique.add(int(str(num)[::-1]))
        return len(unique)