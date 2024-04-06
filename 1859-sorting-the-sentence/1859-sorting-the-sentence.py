class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        string = [' '] * len(words)
        for word in words:
            index = ''
            i = 1
            while word[-i].isdigit():
                index += word[-i]
                word = word[:len(word)-1]
            index = index[::-1]
            string[int(index)-1] = word
            
        return ' '.join(string)
            