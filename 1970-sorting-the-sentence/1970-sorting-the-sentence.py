class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_map = collections.defaultdict(str)
        for word in words:
            word_map[int(word[-1])] = word[:-1]
        return " ".join([word_map[key] for key in sorted(word_map.keys())])