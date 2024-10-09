class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        seq = []
        ans = {}
        
        def bt(idx):
            if len(seq) > 1:ans[tuple(seq)] = 1
                
            for i in range(idx, N):                    
                if not seq or (nums[i] >= seq[-1]):
                    seq.append(nums[i])
                    bt(i+1)
                    seq.pop()
                    
        bt(0)
        return ans.keys()