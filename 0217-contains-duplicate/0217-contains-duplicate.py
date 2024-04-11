class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
        for num in nums:
            if count.get(num) > 1:
                return True
            
        return False