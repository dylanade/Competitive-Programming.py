class Solution:
    def invert(self, s):
        inverted = ""
        for c in s:
            inverted += "0" if c == "1" else "1"
        return inverted
    
    def findS(self, n: int) -> str:
        if n == 1:
            return "0"
        else:
            return self.findS(n-1) + "1" + self.invert(self.findS(n-1))[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.findS(n)[k-1]