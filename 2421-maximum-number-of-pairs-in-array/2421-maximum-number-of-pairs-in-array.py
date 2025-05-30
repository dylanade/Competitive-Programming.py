class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        remove = 0

        for num in nums:
            while count[num] > 1:
                count[num] -= 2
                remove += 1

        print(count)
        return [remove, len(nums) - (remove * 2)]