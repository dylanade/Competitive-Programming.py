class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(words)
        prefix = [0] * (n+1)
        count = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix[i+1] = count

        output = []
        for l, r in queries:
            output.append(prefix[r+1] - prefix[l])
        return output
