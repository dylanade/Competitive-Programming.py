class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return (-1, -1)
        
        def find_first(nums, l, r, target):
            while l < r:
                mid = l+((r-l)//2)
                if nums[mid] < target: l = mid + 1
                elif nums[mid-1] < target: return mid
                else: r = mid - 1
            return l
        
        def find_last(nums, l, r, target):
            while l < r:
                mid = l+((r-l)//2)
                if nums[mid] > target: r = mid - 1
                elif nums[mid+1] > target: return mid
                else: l = mid + 1
            return r
    
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l+((r-l)//2)
            if nums[mid] < target: l = mid + 1
            elif nums[mid] > target: r = mid - 1
            else: 
                return [find_first(nums, 0, mid, target), \
                        find_last(nums, mid, len(nums)-1, target)]
        return (-1, -1)
            
        