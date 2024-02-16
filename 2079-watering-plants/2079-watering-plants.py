class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps, i = 0, 0
        current_capacity = capacity

        while i < len(plants):      
            if current_capacity < plants[i]:
                steps += 2*i    
                current_capacity = capacity
            
            current_capacity -= plants[i]
            steps += 1
            i += 1

        return steps
        