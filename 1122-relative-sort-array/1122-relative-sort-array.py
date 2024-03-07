class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp1, mp2 = {}, {}
        notIn2 = []
        ans = []
        
        for num in arr1:
            mp1[num] = mp1.get(num, 0) + 1
            
        for num in arr2:
            mp2[num] = mp1.get(num)
            
        for key in mp1.keys():
            if key not in arr2:
                for _ in range(mp1.get(key)):
                    notIn2.append(key)
            
        for key in mp2.keys():
            for _ in range(mp2.get(key)):
                ans.append(key)

        return ans + sorted(notIn2)
            