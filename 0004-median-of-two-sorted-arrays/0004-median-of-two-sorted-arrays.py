class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        merged = nums1 + nums2
        merged.sort()
        mn = len(merged)
        half_mn = mn//2
        
        if (mn%2 == 0):
            return float(merged[half_mn] + merged[half_mn-1])/2.0
        else:
            return merged[half_mn]
