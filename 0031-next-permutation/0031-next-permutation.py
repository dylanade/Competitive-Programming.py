class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # find rightmost position i such that L[i] < L[i+1]
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i -= 1
            
        if i == -1:
            nums.reverse()
            return
        
        # find rightmost position j to the right of i such that L[j] > L[i]
        j = i+1
        while j<n and nums[j]>nums[i]:
            j+=1
        j-=1
        
        # swap L[i] and L[j]
        nums[i], nums[j] = nums[j], nums[i]

        # reverse everything to the right of i
        l = i + 1
        r = n - 1
 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
    
