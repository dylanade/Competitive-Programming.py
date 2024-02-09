class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        for item in list1:
            if (item in list2):
                index_1 = list1.index(item)
                index_2 = list2.index(item)
                index_map[item] = index_1 + index_2
        
        index_keys = list(index_map.keys())
        answer = index_keys[0]
        min_index_sum = index_map.get(answer)
        answers = []
        
        for key in index_map:
            value = index_map.get(key)
            if value < min_index_sum:
                min_index_sum = value
                answer = key
            
        for key in index_map:
            if min_index_sum == index_map.get(key):
                answers.append(key)
                
        return answers
            
        