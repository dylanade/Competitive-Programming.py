class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = max(arr)
        peak_pos = arr.index(peak)

        if peak_pos == 0 or peak_pos == len(arr) - 1:
            return False

        i, j = peak_pos-1, peak_pos+1

        prev_down = peak
        while i >= 0:
            if arr[i] >= prev_down:
                return False
            prev_down = arr[i]
            i -= 1

        prev_up = peak
        while j < len(arr):
            if arr[j] >= prev_up:
                return False
            prev_up = arr[j]
            j += 1 

        return True