class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        peak = max(arr)
        peak_pos = arr.index(peak)
        
        i, j = peak_pos, peak_pos

        if peak_pos == 0 or peak_pos == n-1:
            return False

        while i>0:
            if not (arr[i-1]<arr[i]):
                return False
            i -= 1

        while j<n-1:
            if not (arr[j]>arr[j+1]):
                return False
            j += 1

        return True