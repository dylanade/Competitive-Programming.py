class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = len(b) // len(a)
        count = 1
        while count <= repeat + 2:
            if b in a*count:
                return count
            else:
                count += 1
                
        return -1
