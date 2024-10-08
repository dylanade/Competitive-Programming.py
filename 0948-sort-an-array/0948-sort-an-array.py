class Solution:

    def merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

    def mergeSort(self, arr):
        step = 1  # Starting with sub-arrays of length 1
        length = len(arr)
        
        while step < length:
            for i in range(0, length, 2*step):
                left = arr[i : i+step]
                right = arr[i+step : i+2*step]
                
                merged = self.merge(left, right)
                
                # Place the merged array back into the original array
                for j, val in enumerate(merged):
                    arr[i + j] = val
                    
            step *= 2  # Double the sub-array length for the next iteration
            
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)