class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        merged = []
        n = len(nums)
        left = nums[:n//2]
        right = nums[n//2:]
        j, k = 0, 0
        
        for i in range(n):
            if (i%2 == 0):
                merged.append(left[j])
                j+=1
            else:
                merged.append(right[k])
                k+=1
                
        return merged
            