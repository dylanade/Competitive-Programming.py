import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a dictionary to store x-coord of intervals and index 
        start_points = {}
        for i, interval in enumerate(intervals):
            start_points[interval[0]] = i
        
        # Sort the intervals based on their x-coord
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        # Initialize the result list with -1 for all intervals
        result = [-1] * len(intervals)
        
        # Iterate over the sorted intervals
        for i, interval in enumerate(intervals):
            # Find the index of the right interval using binary search
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            
            # If a right interval is found, update the result list with index
            if index != len(intervals):
                result[i] = start_points[sorted_intervals[index][0]]
        
        return result
