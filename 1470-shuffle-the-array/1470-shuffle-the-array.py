class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i, j, k = 0, n, 0
        shuffled = []
        while i < n and j < len(nums):
            shuffled.append(nums[i])
            shuffled.append(nums[j])
            i += 1
            j += 1
            
        return shuffled