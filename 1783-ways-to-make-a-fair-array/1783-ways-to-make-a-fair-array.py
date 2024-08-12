class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even, odd = [0], [0]
        for i in range(len(nums)):
            if(i % 2):
                odd.append(odd[-1] + nums[i])
                even.append(even[-1])
            else:
                even.append(even[-1] + nums[i])
                odd.append(odd[-1])
                
        ans = 0
        for i in range(1, len(nums)+1):
            e_l, o_l = even[i-1], odd[i-1]
            e_r, o_r = even[-1]-even[i], odd[-1]-odd[i]
            if(e_l + o_r == e_r + o_l):
                ans += 1
        return ans