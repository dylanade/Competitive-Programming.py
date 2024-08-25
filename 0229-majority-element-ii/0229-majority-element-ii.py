class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = collections.Counter(nums)
        constraint = int(len(nums)/3)
        answer = []
        for i in frequency:
            if frequency[i] > constraint: 
                answer.append(i)
        return answer