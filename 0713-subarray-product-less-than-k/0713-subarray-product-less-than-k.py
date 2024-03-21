class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        windowSize = 0
        product = 1
        answer = 0
        right = 0
        
        while right < len(nums):
            product *= nums[right]
            
            while product >= k:
                product /= nums[windowSize]
                windowSize += 1
                
            answer += (right - windowSize + 1)
            right += 1
        return answer
    
# This function numSubarrayProductLessThanK takes a vector of integers nums and an integer k as input.
# It initializes variables l, r, product, and count to keep track of the left and right pointers of the sliding window, current product, and the count of subarrays with product less than k.
# It iterates through the array nums using the right pointer r.
# Inside the loop, it updates the product by multiplying it with the element at index r.
# Then, it enters a while loop to adjust the left pointer l while the product is greater than or equal to k. It divides the product by the element at index l and increments l.
# Finally, it updates the count by adding the number of subarrays ending at index r (which is r - l + 1) and continues the iteration.
# Once the loop finishes, it returns the total count of subarrays with product less than k.

# Time complexity: O(n)
# Space complexity: O(1)