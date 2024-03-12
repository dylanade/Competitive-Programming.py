class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # length of longest mountain
        maximum = 0
		
		# length of uphill
        go_up = 0
		
		# length of downhill
        go_down = 0
        
        for i in range(1, len(A)):
            if (go_down and A[i-1]<A[i]) or A[i-1]==A[i]:
                # reset after boundary of current mountain is found
                go_up = 0
                go_down = 0
                
            if A[i-1]<A[i]:
                # current height is higher than previous one
                go_up += 1
            
            if A[i-1]>A[i]:
                # current height is lower than pervious one
                go_down += 1
                
            if go_up and go_down:
                # update with length of current mountain
                maximum = max(maximum, go_up+go_down+1 )
                
        return maximum
            
            