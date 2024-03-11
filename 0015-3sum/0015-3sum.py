class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            new_target = -nums[i]
            while j < k:
                twoSum = nums[j] + nums[k]
                if twoSum < new_target:
                    j += 1
                elif twoSum > new_target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                    while k > j and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
        return res

        
'''
The idea is to first sort nums, and iterate over all possible values nums[i] for the smallest number in the triple. For each value, we need to find a pair nums[j], nums[k] with i < j < k such that nums[j] + nums[k] == -nums[i]. This is just the twoSum problem, and can be solved in O(n) time with two pointers. The overall runtime is thus O(n^2).

Tricks to avoid duplicates:
When we iterate i over range(n-2) to find the smallest number in the triple, if i > 0 and nums[i] == nums[i-1], it means that we have already consider nums[i] to be the smallest number in the triple in the previous iteration. Hence we need to continue and jump to the next iteration. Otherwise, it might leads to duplicate triples.

For each fixed nums[i], we need to use two pointers k > j > i to find a unique pair nums[j], nums[k], such that nums[j]+nums[k] == -nums[i]. We initialize j = i+1, k = len(nums)-1, and increment j by 1 if nums[j]+nums[k] < -nums[i] and decrement k by 1 if nums[j]+nums[k] > -nums[i]. The tricky part is when nums[j]+nums[k] == -nums[i], we first add the triple [nums[i], nums[j], nums[k]] to our result. In order to avoid duplicate triples, we increment j until nums[j] != nums[j-1], and decrement k until nums[k] != nums[k+1]. We continue with the above procedure until j >= k.
Time complexity: O(n^2) 
Space complexity: O(1)
'''