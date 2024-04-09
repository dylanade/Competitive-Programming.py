class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [0] * n
        suf_prod = [0] * n
        result = [0] * n
        
        temp = 1
        for i in range(n):
            pre_prod[i] = temp * nums[i]
            temp *= nums[i]
           
        temp = 1
        for i in range(n-1, -1, -1):
            suf_prod[i] = temp * nums[i]
            temp *= nums[i]
            
        for i in range(n):
            if i == 0:
                result[i] = suf_prod[i+1]
            elif i == n-1:
                result[i] = pre_prod[i-1]
            else:
                result[i] = pre_prod[i-1] * suf_prod[i+1]
                
        return result
        