class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        
        for candy in candies:
            added_candies = candy + extraCandies
            if (added_candies >= max(candies)):
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
        
        