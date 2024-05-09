class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1  

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1 