class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        same_numbers = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])
        min_good = float('inf')
        
        for num in fronts + backs:
            if num not in same_numbers:
                min_good = min(min_good, num)
                
        return min_good if min_good != float('inf') else 0
        