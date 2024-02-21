class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        temp = arr.copy()
        arr.clear()
        
        for num in temp:
            if (len(arr) < n):
                if num == 0:
                    arr.append(0)
                    if (len(arr) < n):
                        arr.append(0)
                else:
                    arr.append(num)  
            else:
                break

            
        