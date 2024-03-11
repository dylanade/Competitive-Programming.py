class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        mp = {}
        check_twoSum = set() #check whether the indices were saved
        answer = []

        for a in range(n):
            for b in range(a+1, n):
                twoSum = nums[a] + nums[b]
                twoSum_tuple = (nums[a], nums[b])
                
                if twoSum_tuple in check_twoSum:
                    continue
                else:
                    check_twoSum.add(twoSum_tuple)
                    if twoSum in mp:
                        mp[twoSum].append((a, b))
                    else:
                        mp[twoSum] = [(a, b)]

        #print(num_to_idx)

        for a in range(n):
            for b in range(a+1, n):
                diff = target - nums[a] - nums[b]
                if diff in mp:
                    for c, d in mp[diff]:
                        if a != c and a != d and b!=c and b!=d:
                            #print([nums[a], nums[b], nums[c], nums[d]])
                            result = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if result not in answer:
                                answer.append(result)
        return answer