class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        string = [' '] * len(words)
        for word in words:
            index = ''
            while word[-1].isdigit():
                index += word[-1]
                word = word[:len(word)-1]
            index = index[::-1]
            string[int(index)-1] = word
            
        return ' '.join(string)
            