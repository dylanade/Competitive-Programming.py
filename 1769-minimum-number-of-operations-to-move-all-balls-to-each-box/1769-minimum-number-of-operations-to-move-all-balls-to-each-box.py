class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        indices = []
        answer = []
        
        for i, box in enumerate(boxes):
            if (box == '1'):
                indices.append(i)
        
        for i in range(n):
            count = 0
            for j in indices:
                count += abs(i-j)
            answer.append(count)
            
        return answer