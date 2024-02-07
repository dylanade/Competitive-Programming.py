class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = dict()
        
        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        
        for key in dictionary:
            if (dictionary.get(key) == 1):
                return key
        
        return -1
        