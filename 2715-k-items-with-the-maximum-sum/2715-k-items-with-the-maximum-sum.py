class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0

        while k:
            if numOnes > 0:
                answer += 1
                numOnes -= 1
            elif numZeros > 0:
                numZeros -= 1
            elif numNegOnes > 0:
                answer -= 1
                numNegOnes -= 1
            k -= 1

        return answer
        