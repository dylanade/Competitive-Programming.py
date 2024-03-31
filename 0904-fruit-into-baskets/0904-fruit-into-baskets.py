class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        max_fruit = 0
        # starting point of window
        l = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            #if size is greater than 2, remove the elements of same type that added first
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            max_fruit = max(max_fruit, r-l+1)    
               
        return max_fruit
            
# Intuition
# Have to: Find the maximum number of fruits that can be placed into the two basket such that each contains only one type of fruit and we have to also ensures that if we have reach at a point where we can't take fruit i.e third type of fruit, we must stop at that point.
# S we use sliding window approach to solve this problem as we have to find the maximum window number of fruit from each tree.

# Time complexity: O(n)
# Space complexity: O(1)
