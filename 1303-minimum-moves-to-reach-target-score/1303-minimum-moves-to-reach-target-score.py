class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count_moves = 0
        
        while maxDoubles and target > 1:
            if target % 2 == 0 and maxDoubles:
                count_moves += 1
                maxDoubles -= 1
                target //= 2
            else:
                target -= 1
                count_moves += 1

        if target > 1:
            count_moves += target - 1

        return count_moves 