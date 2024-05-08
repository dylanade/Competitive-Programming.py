class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        answer = []
        for word in words:
            char_word = list(set(word.lower()))
            count = 0
            if char_word[0] in first_row:
                for c in char_word:
                    if c in first_row:
                        count += 1
                if count == len(char_word):
                    answer.append(word)
            elif char_word[0] in second_row:
                for c in char_word:
                    if c in second_row:
                        count += 1
                if count == len(char_word):
                    answer.append(word)
            elif char_word[0] in third_row:
                for c in char_word:
                    if c in third_row:
                        count += 1
                if count == len(char_word):
                    answer.append(word)
                        
        return answer