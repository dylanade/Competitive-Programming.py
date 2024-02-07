class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_index = {}

        for i in range(len(nums)):
            if nums[i] in map_index:
                if abs(map_index[nums[i]] - i) <= k:
                    return True

            map_index[nums[i]] = i

        return False
        
        