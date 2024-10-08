class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # answer = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     answer.append(count)

        # return answer

        # O(n^2) -> O(nlogn)

        arr, ans = sorted(nums), []          
        
        for num in nums:
            i = bisect_left(arr, num)          
            ans.append(i)                     
            del arr[i]                       
            
        return ans                            