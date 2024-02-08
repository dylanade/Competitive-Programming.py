class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictionary = {}
        
        for i in range(len(matches)):
            if (matches[i][0] in dictionary):
                dictionary[matches[i][0]].append(True)
            else:
                dictionary[matches[i][0]] = [True]
                
            if (matches[i][1] in dictionary):
                dictionary[matches[i][1]].append(False)
            else:
                dictionary[matches[i][1]] = [False]     
        
        win, loss = [], []
        for key in dictionary:
            value = dictionary.get(key)
            if (len(value) == sum(value)):
                win.append(key)
            elif (len(value)-1 == sum(value)):
                loss.append(key)
                
        win.sort()
        loss.sort()

        return [win, loss]
            
        