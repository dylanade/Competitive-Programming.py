class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Result list to store the pairs
        res = []  
        # Priority queue to store pairs with smallest sums, sorted by the sum
        pq = []  

        # Push the initial pairs into the priority queue
        for x in nums1:
            # The sum and the index of the second element in nums2
            heapq.heappush(pq, [x + nums2[0], 0])  

        # Pop the k smallest pairs from the priority queue
        while k > 0 and pq:
            pair = heapq.heappop(pq)

            # Get the smallest sum and the index of the second element in nums2
            min_sum, pos = pair[0], pair[1]  

            # Add the pair to the result list
            res.append([min_sum - nums2[pos], nums2[pos]])  

            # If there are more elements in nums2, push the next pair into the priority queue
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [min_sum - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  

        # Return the k smallest pair
        return res