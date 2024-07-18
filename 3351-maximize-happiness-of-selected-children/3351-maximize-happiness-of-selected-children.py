class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        answer = 0
        i = 0
        reduction = 0

        while k:
            if happiness[i] - reduction > 0:
                answer += (happiness[i] - reduction)
            reduction += 1
            i += 1
            k -= 1

        return answer
            