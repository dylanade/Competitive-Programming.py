class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mp = {}
        
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        nums.clear()
        for key in mp.keys():
            if mp.get(key) > 1:
                nums.append(key)
                nums.append(key)
            else:
                nums.append(key)
                
        return len(nums)
        