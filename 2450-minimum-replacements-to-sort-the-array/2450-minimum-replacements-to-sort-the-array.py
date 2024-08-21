class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        last = nums[-1] 
        for num in nums[:-1][::-1]:
            if num <= last:
                last = num
            else:
                div = num // last
                
                if num % last:
                    div += 1
                    
                answer += div - 1
                last = num // div

        return answer