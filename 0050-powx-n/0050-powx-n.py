class Solution:
    def myPow(self, x: float, n:int) -> float:
        # TLE: 291/307 TC
        # is_negative = n < 0
        # n = -n if is_negative else n

        # answer = 1
        # for _ in range(n):
        #     answer *= x
        # return 1/answer if is_negative else answer

        # DIVIDE and CONQUER 2^10 -> 2^5 * 2^5 = 2^10
        # cutting the work in half each time: O(log2(n))

        def helper(x, n):
            if x == 0: return 0 # any number powered to 0 is 0
            if n == 0: return 1 
        
            answer = helper(x, n//2)
            answer = answer * answer
            return x * answer if n % 2 else answer

        answer = helper(x, abs(n))
        return 1/answer if n < 0 else answer


        