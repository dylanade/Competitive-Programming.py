class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        return [(candy + extra) >= max(candies) for candy in candies]
            