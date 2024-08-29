class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        num_str = [""] * n
        for i, num in enumerate(nums):
            num_str[i] = str(num)
        
        for i in range(n):
            for j in range(i + 1, n):
                if int(num_str[i] + num_str[j]) < int(num_str[j] + num_str[i]):
                    num_str[i], num_str[j] = num_str[j], num_str[i]
        
        ans = ''.join(num_str)
        return "0" if int(ans) == 0 else ans