class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for num in nums1:
            index_num = nums2.index(num)
            RHS_list = nums2[index_num:]
            RHS_list = [RHS_num for RHS_num in RHS_list if RHS_num > num]
            
            if len(RHS_list) != 0:
                ans.append(RHS_list[0])
            else:
                ans.append(-1)
                
        return ans
            
            
            
            
            
            
            
        
        