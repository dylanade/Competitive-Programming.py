from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        for key, a in Counter(t).items():
            if a > c[key]:
                return key