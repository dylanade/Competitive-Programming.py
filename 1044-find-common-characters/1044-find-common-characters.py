class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        count = dict()
        for dec in range(97, 122 + 1):
            count[chr(dec)] = [0] * len(words)

        print(count)
        for i, word in enumerate(words):
            for char in word:
                count[char][i] += 1 

        print(count)
        answer = []
        for char in count:
            min_count = min(count[char])
            for _ in range(min_count):
                answer.append(char)

        return answer


        