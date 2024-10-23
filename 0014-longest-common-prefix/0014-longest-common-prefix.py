class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 0
        sequence = ""
        sort = sorted(strs)
        first = sort[0]
        last = sort[-1]

        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return sequence
            sequence += first[i]
            
        return sequence
        
        
