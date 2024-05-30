class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # TLE: 1062/1068 TC passed
        # n = len(nums)
        # answer = [0] * n
        # for i in range(n):
        #     total = 0
        #     for j in range(n):
        #         if nums[i] == nums[j]:
        #             total += abs(i - j)
        #     answer[i] = total
        # return answer

        map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            map[num].append(i)

        answer = [0] * len(nums)

        for num, val in map.items():
            suffix_sum = sum(val)
            preffix_sum = 0
            s = len(val)
            p = 0

            for i in val:
                preffix_sum += i
                suffix_sum -= i
                p += 1
                s -= 1
                answer[i] = -preffix_sum + p*i - s*i + suffix_sum

        return answer
