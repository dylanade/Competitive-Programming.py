class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1c = collections.Counter(s1)
        s2c = collections.Counter(s2)

        pos_wrong = 0

        for i in range(len(s1)):
            if s1c[s1[i]] != s2c[s1[i]]:
                return False
            if s1[i] != s2[i]:
                pos_wrong += 1

        return pos_wrong <= 2 