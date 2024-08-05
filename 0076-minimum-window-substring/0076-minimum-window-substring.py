import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        counter = collections.Counter(t)
        window = {}

        have, need = 0, len(counter)
        result, length = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in counter and window[c] == counter[c]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < length:
                    result = [l, r]
                    length = (r - l + 1)

                # pop from left of window
                window[s[l]] -= 1

                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1

                l += 1

        l, r = result

        return s[l:r+1] if length != float("inf") else ""
