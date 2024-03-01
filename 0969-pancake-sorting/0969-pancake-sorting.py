class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        
        while n > 0:
            #choosing k = n-1
            max_element = max(arr[:n])
            max_index = arr[:n].index(max_element)
            
            if max_index+1 == n:
                n -= 1
            else:
                ans.append(max_index+1)
                arr[:max_index+1] = arr[:max_index+1][::-1]
                ans.append(n)
                arr[:n] = arr[:n][::-1]
                n -= 1
                
        return ans
        
            
        
        