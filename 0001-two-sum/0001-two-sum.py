class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        
        for i in range(len(nums)):
            if (int(target - nums[i]) in mapping.keys()):
                return [mapping.get(target-nums[i]), i]
            mapping[nums[i]] = i
            
        return []