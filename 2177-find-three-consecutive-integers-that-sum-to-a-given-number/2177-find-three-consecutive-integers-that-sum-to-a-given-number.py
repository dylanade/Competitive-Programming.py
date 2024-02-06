class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ''' O(n)
        count = 0
        ans = []
        
        for i in range(num):
            ans.append(i)
            
            if count == 3 and sum(ans) != num:
                count = 0
                ans = []
            elif count == 3 and sum(ans) == num:
                return ans
            
            count += 1
            
        return ans
        '''
        
        #O(1)
        '''
            we are looking for (x) + (x+1) + (x+2) == num
            3x + 3 = num
            3x = num-3
            x = (num-3)/3
            if x is not a float, return [x, x+1, x+2] otherwise return []
        '''
        
        x = (num-3) / 3
        
        #check if x is a whole number
        if floor(x) == ceil(x):
            return [int(x), int(x+1), int(x+2)]
        else:
            return []
                