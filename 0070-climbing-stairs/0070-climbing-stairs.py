class Solution:
    def climbStairs(self, n: int) -> int:
        save = {}
        def climb(n):
            if n == 0 or n == 1:
                return 1
            if n not in save:
                save[n] = climb(n-1) + climb(n-2)
            return save[n]

        return climb(n)