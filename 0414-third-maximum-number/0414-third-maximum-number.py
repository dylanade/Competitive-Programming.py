class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        #remove duplicates from the list by initializing a set with nums
        nums = list(set(nums))
        
        #sort the set list
        nums.sort()
        
        #get the lenght of set list
        n = len(nums)
        
        #if the length of set list >= 3 then return the the 3rd last element otherwise max
        if (n >= 3):
            return nums[n-3]
        else:
            return max(nums)
        
        