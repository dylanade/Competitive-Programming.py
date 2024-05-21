# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, m_arr: 'MountainArray') -> int:
        # STEP 1: Find the peak of the array
        # peak: L < P > R
        
        l, r = 1, m_arr.length()-2
        while l <= r:
            mid = (l + r) // 2
            left = m_arr.get(mid - 1)
            peak = m_arr.get(mid)
            right = m_arr.get(mid + 1)

            if left < peak < right:
                l = mid + 1
            elif left > peak > right:
                r = mid - 1
            else:
                peak_index = mid
                break
        
        if peak == target:
            return peak_index

        def find_target_on_left(peak_index, target, m_arr):
            l, r = 0, peak_index
            while l <= r:
                mid = (l + r) // 2
                mid_val = m_arr.get(mid)

                if mid_val < target:
                    l = mid + 1
                elif mid_val > target:
                    r = mid - 1
                else:
                    return mid
            return -1 

        def find_target_on_right(peak_index, target, m_arr):
            l, r = peak_index, m_arr.length()-1
            while l <= r:
                mid = (l + r) // 2
                mid_val = m_arr.get(mid)

                if mid_val > target:
                    l = mid + 1
                elif mid_val < target:
                    r = mid - 1
                else:
                    return mid
            return -1 

        if peak == target:
            return peak_index
        else:
            left = find_target_on_left(peak_index, target, m_arr)
            if left != -1:
                return left
            return find_target_on_right(peak_index, target, m_arr)

            