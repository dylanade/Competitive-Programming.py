class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        distribution = [0] * num_people
        n = 0
        while candies > 0:
            distribution[n % num_people] += min(candies, n+1)
            n += 1
            candies -= n
            
        return distribution
            
            
        