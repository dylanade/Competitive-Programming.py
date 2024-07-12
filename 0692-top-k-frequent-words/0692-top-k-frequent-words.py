class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word
        count = Counter(words)

        # Step 2: Use a heap to keep track of the top k elements
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        
        # Step 3: Extract the top k elements from the heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        
        return result