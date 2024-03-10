class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        snums = set()
        
        for num in nums:
            if num not in snums:
                snums.add(num)
            else:
                ans.append(num)
    
        return ans
            