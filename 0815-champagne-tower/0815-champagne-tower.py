class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # SIMULATION
        # query_row - 0-indexed
        # query_glass - 0-indexed

        # TREE 
        # store each level as an array

        # take half of parent for each child

        prev_row = [poured] # 1, 2, 3 ... , n

        for row in range(1, query_row + 1):
            cur_row = [0] * (row + 1)

            for i in range(row):
                excess = prev_row[i] - 1
                poured_over = 0.5 * excess

                if excess > 0:
                    cur_row[i] += poured_over
                    cur_row[i + 1] += poured_over

            prev_row = cur_row

        return min(1, prev_row[query_glass])