class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occur_map = {}
        
        for num in nums:
            occur_map[num] = occur_map.get(num, 0) + 1
        
        for key in occur_map:
            if (occur_map.get(key) > 1):
                return True
            
        return False
        