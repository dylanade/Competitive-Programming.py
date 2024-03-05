class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(numbers):
            s = target - num
            if s in mp:
                return [mp[s]+1, i+1]
            mp[num] = i
        