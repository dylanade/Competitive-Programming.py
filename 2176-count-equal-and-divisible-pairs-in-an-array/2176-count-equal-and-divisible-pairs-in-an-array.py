class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        mapping = {}
        for i, num in enumerate(nums):
            if num in mapping:
                for j in mapping[num]:
                    if (i*j)%k == 0:
                        count += 1
                mapping[num].append(i)
            else:
                mapping[num] = [i]
        return count
    
    
#         count = 0
#         check = set()
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     if (i*j)%k == 0 and (i, j) not in check:
#                         count += 1
#                         check.add((i, j))
                    
#         return count


        