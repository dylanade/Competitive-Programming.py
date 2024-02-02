class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = 0

        for word in strs:
            sequence = ""
            sort = sorted(strs)
            first = sort[0]
            last = sort[-1]

            for i in range(min(len(first), len(last))):
                if (first[i] != last[i]):
                    return sequence
                sequence += first[i]
            return sequence

#LINK: https://leetcode.com/problems/longest-common-prefix/submissions/1163296112
