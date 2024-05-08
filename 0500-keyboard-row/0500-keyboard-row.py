class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        answer = []
        row = ""
        
        for word in words:
            if word[0].lower() in first_row:
                row = first_row
            elif word[0].lower() in second_row:
                row = second_row
            else:
                row = third_row
            answer.append(word)
            for c in word: 
                if c.lower() not in row:
                    answer.pop(-1)
                    break
                    
        return answer