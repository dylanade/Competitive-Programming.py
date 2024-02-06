class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        
        #search through the list and keep track of the 1's
        for num in nums:
            
            #if element is 1 inc counter
            if num == 1:
                count+=1
            
            #else if not 1 reset the counter but compare the consecutive count
            else:
                max_count = max(max_count, count)
                count = 0
                
        return max(max_count, count)
        