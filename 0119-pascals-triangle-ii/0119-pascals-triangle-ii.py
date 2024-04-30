class Solution:
    def getRow(self, row: int) -> List[int]:
        pascal = [1] * (row+1)
        if row < 2:
            return pascal
        p_pascal = self.getRow(row-1)
        for i in range(row-1):
            pascal[i+1] = p_pascal[i] + p_pascal[i+1]
        return pascal