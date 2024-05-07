class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [-math.inf] + A + [-math.inf]
        n = len(A)

        stack = []
        ans = 0

        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                mid = stack.pop()
                left = stack[-1]  # previous smaller element
                right = i  # next smaller element
                ans += A[mid] * (mid - left) * (right - mid)
            stack.append(i)

        return ans % (10**9 + 7)