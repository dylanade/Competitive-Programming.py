class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
            
        for key in mp.keys():
            if mp.get(key) > 1:
                return key
        
        return -1
        
        