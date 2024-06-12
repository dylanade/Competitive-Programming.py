class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than, equal_to, greater_than = [], [], []

        for num in nums:
            if num < pivot: less_than.append(num)
            if num > pivot: greater_than.append(num)
            if num == pivot: equal_to.append(num)

        return less_than + equal_to + greater_than