class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            list_word = list(word)
            if (list_word == list_word[::-1]):
                return word
            
        return ""
        