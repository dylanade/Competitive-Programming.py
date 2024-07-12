class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.defaultdict(list)

        for word in words:
            count = words.count(word)
            if word not in freq[count]:
                freq[count].append(word)

        answer = []
        for frequency in sorted(freq, reverse=True):
            for word in sorted(freq[frequency]):
                if k:
                    answer.append(word)
                    k -= 1
                else:
                    return answer

        return answer


        