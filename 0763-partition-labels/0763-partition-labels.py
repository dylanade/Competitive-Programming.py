class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        substring = 0
        # pointing to the starting of a substring
        j = 0
        last = {}
        ans = []
        
        for i in range(len(s)):
            last[s[i]] = i # take last occurence of every element

        for i in range(len(s)):
            substring = max(substring, last[s[i]])
            if substring == i:
                ans.append(i-j+1)
                j = i + 1

        return ans
        