import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        check = set() #check whether the indices were saved
        save = collections.defaultdict(list)
        answer = []

        for a in range(n):
            for b in range(a+1, n):
                two_sum = nums[a] + nums[b]
                sum_tuple = (nums[a], nums[b])
                if sum_tuple not in check:
                    check.add(sum_tuple)
                    if (a, b) not in save[two_sum]:
                        save[two_sum].append((a, b))

        for a in range(n):
            for b in range(a+1, n):
                diff = target - nums[a] - nums[b]
                if diff in save:
                    for c, d in save[diff]:
                        if a!=c and a!=d and b!=c and b!=d:
                            result = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if result not in answer:
                                answer.append(result)
        return answer