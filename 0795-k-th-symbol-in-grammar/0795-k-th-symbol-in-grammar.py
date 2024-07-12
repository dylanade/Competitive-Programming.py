class Solution:
    # TLE
    # def replace(self, s):
    #     row = ""
    #     for c in s:
    #         row += "01" if c == "0" else "10"
    #     return row
                
    # def findGrammar(self, n):
    #     if n == 1:
    #         return "0"
    #     else:
    #         return self.replace(self.findGrammar(n-1))
        
    def kthGrammar(self, n: int, k: int) -> int:
        # TLE: O(2^(n-1))
        # return int(self.findGrammar(n)[k-1])

        # an observation: building a BST: O(h) where h is height
        current = 0
        l, r = 1, 2**(n-1)

        for _ in range(n-1):
            mid = (l + r) // 2
            if k <= mid:    #left half
                r = mid
            else:           #right half
                l = mid + 1
                current = 0 if current else 1
                
        return current