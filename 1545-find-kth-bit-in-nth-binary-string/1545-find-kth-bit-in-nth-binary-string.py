class Solution:
    def invert(self, s):
        inverted = ""
        for c in s:
            inverted += "0" if c == "1" else "1"
        return inverted
    
    def reverse(self, s):
        return s[::-1]
    
    def findBinaryString(self, n: int) -> str:
        if n == 1:
            return "0"
        else:
            result = self.findBinaryString(n-1)
            return (result+"1"+self.reverse(self.invert(result)))
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.findBinaryString(n)[k-1]