class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
        
        ## Sorting operation: O(n*log(n))
        # nums.sort(reverse=True)
        # return nums[k-1]

        # Using max heap: O(n+k*log(n))

        # # Quick Select: Avg Case Time Complexity: O(n) with worst case: O(n*2) 
        # k = len(nums) - k

        # def quickSelect(l, r):
        #     pivot, p = nums[r], l

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1

        #         nums[p], nums[r] = nums[r], nums[p]

        #         if p>k: 
        #             return quickSelect(l, p-1)
        #         elif p<k: 
        #             return quickSelect(p+1, r)
        #         else: #p == k
        #             return nums[p]

        # return quickSelect(0, len(nums) - 1)

