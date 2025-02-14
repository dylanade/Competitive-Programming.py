class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        x = -1
        y = -1
        ans = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                y = i
            elif wordsDict[i] == word2:
                x = i

            if x != -1 and y != -1:
                ans = min(ans, abs(y - x)) 
                    
        return ans
        

