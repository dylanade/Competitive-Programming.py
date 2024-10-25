class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float("inf") # trying to minimize
        pairs = [] # (ratio, quality)
        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))
        pairs.sort(key=lambda p:p[0])

        maxHeap = [] # qualities
        total_quality = 0

        for rate, q in pairs:
            heapq.heappush(maxHeap, -q)
            total_quality += q
            if len(maxHeap) > k:
                n = heapq.heappop(maxHeap)
                total_quality += n
            if len(maxHeap) == k:
                res = min(res, total_quality * rate)

        return res