class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        from sortedcontainers import SortedList
        n, pairs = len(nums1), 0
        # simplify the problem by rearranging equations: find all pairs of i, j in nums such that nums[i] - nums[j] <= diff
        nums = [x1 - x2 for x1, x2 in zip(nums1, nums2)] # condense to one list
        # look back thru sorted list to find number of past i's such that nums[i] <= nums[j] + diff
        i_nums = SortedList()      
        for j_num in nums:
            pairs += i_nums.bisect_right(j_num + diff)
            i_nums.add(j_num)
			
        return pairs