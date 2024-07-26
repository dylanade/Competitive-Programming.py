class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s) # O(n)
        
        maxHeap = [(-count, char) for char, count in counter.items()] # O(log(n)) -> O(n) > O(log(n)) TC = O(n)
        heapq.heapify(maxHeap)  # SC -> O(n)
        
        prevChar = ""
        prevFreq = 0
        
        result = [] # return # SC -> O(n)
        
        while maxHeap:  # TC -> O(n)
            count, char = heapq.heappop(maxHeap)
            result.append(char)
            
            # if the prevFreq of prevChar is greater than 0, push it back to the heap
            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))
            
            prevFreq = count + 1
            prevChar = char
            
        if len(result) != len(s):
            return ""
        else:
            return "".join(result)
            
        # TC: O(n)
        # SC: O(n)