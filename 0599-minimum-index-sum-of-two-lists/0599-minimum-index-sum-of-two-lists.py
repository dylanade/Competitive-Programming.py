class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {} #dict {key:value}
                        #key = the common element from list1 and list2
                        #value = index_sum (index_from_list1 + index_from_list2)
        
        for item in list1:
            if (item in list2):
                index_1 = list1.index(item)
                index_2 = list2.index(item)
                index_map[item] = index_1 + index_2

        index_values = list(index_map.values())
        min_index_sum = min(index_values)
        answers = []

        for key in index_map:
            if index_map.get(key) == min_index_sum :
                answers.append(key)
                
        return answers
            
        