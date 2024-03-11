class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        num_to_idx = {}
        vals = set()
        answer=[]

        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                val = nums[a] + nums[b]
                value_tuple = (nums[a], nums[b])
                if value_tuple in vals:
                    continue
                else:
                    vals.add(value_tuple)
                    if val in num_to_idx:
                        num_to_idx[val].append((a, b))
                    else:
                        num_to_idx[val] = [(a, b)]

        #print(num_to_idx)

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                diff = target - nums[a] - nums[b]
                if diff in num_to_idx:
                    for c, d in num_to_idx[diff]:
                        if a != c and a != d and b!=c and b!=d:
                            #print([nums[a], nums[b], nums[c], nums[d]])
                            res = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if res not in answer:
                                answer.append(res)


        return answer