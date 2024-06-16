class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_capacity = capacity

        for i in range(len(plants)):   
            if current_capacity < plants[i]:
                steps += 2 * i    
                current_capacity = capacity
            
            current_capacity -= plants[i]
            steps += 1

        return steps

        