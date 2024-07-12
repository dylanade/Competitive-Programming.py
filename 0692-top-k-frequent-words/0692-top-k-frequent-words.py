class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return result