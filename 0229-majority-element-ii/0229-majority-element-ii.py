class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occur_map = {}
        answer = []
        constraint = int(len(nums)/3) #n = len(nums) check: occurence > [n/3]
        
        for num in nums:
            occur_map[num] = occur_map.get(num, 0) + 1
            
        for key in occur_map:
            if (occur_map.get(key) > constraint):
                answer.append(key)
                
        return answer
        
        