class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            distance_apart_x = abs(target[0] - ghost[0])
            distance_apart_y = abs(target[1] - ghost[1])
            distance_apart = distance_apart_x + distance_apart_y
            target_distance = abs(target[0]) + abs(target[1])
            
            if (distance_apart <= target_distance):
                return False
            
        return True