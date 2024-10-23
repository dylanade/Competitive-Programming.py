class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sequence = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return sequence
            sequence += first[i]
            
        return sequence
        
        
