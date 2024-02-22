class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_score = nums.count(1)
        indices = [0]
        curr_score = max_score
        
        for i, num in enumerate(nums):
            if num == 0:
                curr_score += 1
            else:
                curr_score -= 1
                
            if curr_score > max_score:
                max_score = curr_score
                indices = [i+1]
            elif curr_score == max_score:
                indices.append(i+1)
                
        return indices

            
        