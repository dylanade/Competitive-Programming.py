class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_capacity = capacity

        for i, plant in enumerate(plants):   
            if current_capacity < plant:
                steps += 2*i    
                current_capacity = capacity
            
            current_capacity -= plant
            steps += 1

        return steps

        