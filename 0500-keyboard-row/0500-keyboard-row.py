class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        answer = []
        
        for word in words:
            chars = set(word.lower())
            if chars.issubset(firstRow) \
            or chars.issubset(secondRow) \
            or chars.issubset(thirdRow):
                answer.append(''.join(word))
                
        return answer
            
        
        