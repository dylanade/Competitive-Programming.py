class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        answer = 0
        for x in nums: answer ^= x
        return answer