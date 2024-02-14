class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        merged = []
        
        j, k = 0, 0
        for i in range(len(nums)):
            if (i%2 == 0):
                merged.append(positive[j])
                j+=1
            else:
                merged.append(negative[k])
                k+=1
        
        return merged
        
        