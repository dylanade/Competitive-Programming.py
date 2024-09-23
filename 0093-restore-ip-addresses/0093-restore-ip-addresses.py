class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 3^12

        # 256 choices for each of the spots BUT
        # order of s stays same
        # just put "." inbetween

        res = []

        if len(s) > 12:
            return res

        def backtrack(i, numDot, curIP):
            if numDot == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            
            if numDot > 4:
                return

            for j in range(i, min(i+3, len(s))):
                                            # no leading zeros
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j+1, numDot+1, curIP + s[i:j+1] + ".")

        backtrack(0, 0, "")
        return res