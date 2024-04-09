class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count, current_sum = 0, 0

        for num in nums:
            current_sum += num
            remainder = current_sum%k
            if remainder in hashmap:
                count += hashmap[remainder] 
            hashmap[remainder] += 1
        
        return count