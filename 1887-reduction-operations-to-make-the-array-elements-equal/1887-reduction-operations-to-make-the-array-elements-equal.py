class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        else:
            count = {}
            nums.sort(reverse=True)
            
            #freq dictionary keep track of freq's
            for num in nums:
                count[num] = count.get(num, 0) + 1
            
            #total number of operations required
            operations = 0
            changes = 0
            
            for num in sorted(count, reverse=True):
                count[num] += changes
                operations += count[num]
                changes = count[num]
            
            return operations-changes
                
            
            
            
        
            
            
            
            
            
            
        