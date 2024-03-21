from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for i in count.keys():
            if count.get(i) > 1:
                return i
            
        return -1
            
        