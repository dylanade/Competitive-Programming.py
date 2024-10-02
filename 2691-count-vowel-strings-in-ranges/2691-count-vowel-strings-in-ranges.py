class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries)
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        prefix_sum = [0] * (len(words) + 1)
        count = 0
        for i, word in enumerate(words):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
            prefix_sum[i] = count

        for i, query in enumerate(queries):
            l, r = query
            answer[i] = prefix_sum[r] - prefix_sum[l - 1]

        return answer
