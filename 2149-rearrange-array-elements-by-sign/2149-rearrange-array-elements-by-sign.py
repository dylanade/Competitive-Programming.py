class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        merged = []
        
        for num in nums:
            if (num < 0):
                negative.append(num)
            else:
                positive.append(num)
        
        j,k = 0,0
        for i in range(len(nums)):
            if (i%2 == 0):
                merged.append(positive[j])
                j+=1
            else:
                merged.append(negative[k])
                k+=1
        
        return merged
        
        