class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        for char, freq in tc.items():
            if freq > sc[char]:
                return char