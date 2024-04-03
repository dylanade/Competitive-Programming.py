class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l = 0
        count_T = count_F = answer = 0
        
        for r in range(n):
            count_T += answerKey[r] == 'T'
            count_F += answerKey[r] == 'F'
                
            while count_T > k and count_F > k:
                count_T -= answerKey[l] == 'T'
                count_F -= answerKey[l] == 'F'
                l += 1
                
            answer = max(answer, r-l+1)
            
        return answer
        