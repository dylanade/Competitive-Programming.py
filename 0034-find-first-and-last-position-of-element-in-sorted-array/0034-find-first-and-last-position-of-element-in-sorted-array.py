class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bisect_left = bisect.bisect_left

        if len(nums) == 0:
            return [-1,-1]

        first = bisect_left(nums, target)        
        if first<0 or first>=len(nums) or nums[first]!=target:
            return [-1,-1]

        last = bisect_left(nums, target+1) -1
        if last<0 or last>=len(nums) or nums[last]!=target:
            return [-1,-1]

        return [first,last] 
            
        