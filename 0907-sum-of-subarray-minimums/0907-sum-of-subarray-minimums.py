class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        stack = []  
        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop() 
                left = stack[-1] if stack else -1
                right = i 
                count = (mid - left) * (right - mid)
                curr_min = arr[mid]
                ans += curr_min * count
            stack.append(i)

        return ans % int(1e9 + 7)  
#     class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         N = len(arr)
#         ans = 0
#         stk = []  # Stack to keep track of indices
#         for idx in range(N+1):
#             # Iterate through the array, including an extra iteration at the end
#             while stk and (idx == N or arr[stk[-1]] >= arr[idx]):
#                 mid = stk.pop()  # The top one, which is the middle index in the current subarray 
#                 left = stk[-1] if stk else -1  # Index of the previous smaller number
#                 right = idx  # Current index
#                 # Calculate the count of subarrays where arr[mid] is the minimum
#                 # left, exclusive; right, inclusive, 
#                 # because left is the previous smaller number index
#                 count = (mid - left) * (right - mid)
#                 curMin = arr[mid]
#                 ans += curMin * count
#             # Push the current index onto the stack, 
#             # whose indices point to numbers are non-decreasing
#             stk.append(idx)

#         return ans % int(1e9 + 7)  # Return the result modulo 1e9 + 7
