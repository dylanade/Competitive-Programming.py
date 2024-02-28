class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_mp = {}
        answer = []
        constraint = int(len(nums)/3) #n = len(nums) check: occurence > [n/3]
        
        for num in nums:
            freq_mp[num] = freq_mp.get(num, 0) + 1
            
        for key in freq_mp:
            if freq_mp.get(key) > constraint:
                answer.append(key)
                
        return answer
        
        