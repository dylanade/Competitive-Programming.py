class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_1 = ''.join(word1)
        word_2 = ''.join(word2)
        return word_1.lower() == word_2.lower()
        