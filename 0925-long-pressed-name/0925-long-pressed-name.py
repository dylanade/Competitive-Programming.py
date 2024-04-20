import collections
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n, m = len(typed), len(name)

        while j < n:
            if i < m and name[i] == typed[j]:
                i += 1
                j +=1
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False

        return i == m