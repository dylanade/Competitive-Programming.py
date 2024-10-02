class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        is_vowels = [False] * len(words)
        for i, word in enumerate(words):
            if words[i][0] in vowels and words[i][-1] in vowels:
                is_vowels[i] = True

        prefix_sum = [0] * (len(words) + 1)
        total = 0
        for i in range(len(words)):
            total += is_vowels[i]
            prefix_sum[i] = total

        print(prefix_sum)
        for i, query in enumerate(queries):
            l, r = query
            answer.append(prefix_sum[r] - prefix_sum[l - 1])

        return answer
