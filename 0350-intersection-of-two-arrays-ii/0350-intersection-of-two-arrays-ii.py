class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp1 = {}
        mp2 = {}
        inter = []
        
        for num in nums1:
            mp1[num] = mp1.get(num, 0) + 1
        
        for num in nums2:
            mp2[num] = mp2.get(num, 0) + 1
            
        for key in mp1:
            for _ in range(min(mp1.get(key, 0), mp2.get(key, 0))):
                inter.append(key)
                
        return inter
        