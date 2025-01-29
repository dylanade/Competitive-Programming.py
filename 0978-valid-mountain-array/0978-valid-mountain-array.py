class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        peak = max(arr)
        peak_pos = arr.index(peak)

        if peak_pos == 0 or peak_pos == n-1:
            return False

        i = j = peak_pos

        while i > 0 and arr[i] > arr[i-1]:
            i -= 1

        while j < n-1 and arr[j] > arr[j+1]:
            j += 1

        return i == 0 and j == n-1