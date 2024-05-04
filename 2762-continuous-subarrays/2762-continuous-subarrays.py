class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # maintain two queues
        # one monotonically increasing q for smallest elements
        # one monotonically decreasing q for the biggest elements
        # everytime you consider an element:
        # check if the diff between the smallest/biggest exceeds the limit
        answer = 1
        smallest = deque([0])
        biggest = deque([0])
        
        #l points to the left of the window
        l = -1
        for r in range(1, len(nums)):
            while smallest and abs(nums[smallest[0]] - nums[r]) > 2:
                l = max(l, smallest.popleft())
            while biggest and abs(nums[biggest[0]] - nums[r]) > 2:
                l = max(l, biggest.popleft())
                
            answer += r-l
            while smallest and nums[r] < nums[smallest[-1]]: 
                smallest.pop()
            while biggest and nums[r] > nums[biggest[-1]]: 
                biggest.pop()
            smallest.append(r)
            biggest.append(r)
            
        return answer
                
        
        