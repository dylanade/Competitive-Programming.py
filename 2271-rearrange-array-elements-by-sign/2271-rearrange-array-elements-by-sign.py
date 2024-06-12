class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num < 0: neg.append(num)
            if num > 0: pos.append(num)

        j, k = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0: 
                nums[i] = pos[j]
                j += 1
            else:
                nums[i] = neg[k]
                k += 1
        return nums