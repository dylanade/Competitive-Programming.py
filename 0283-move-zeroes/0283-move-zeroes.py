class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # for num in nums:
        #     if num == 0:
        #         nums.append(num)
        #         nums.remove(num)
        
        #Using Two-Pointers Seeker and Placeholder
        
        holder = 0
        seeker = 0
        
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1
            
        
                
        
        