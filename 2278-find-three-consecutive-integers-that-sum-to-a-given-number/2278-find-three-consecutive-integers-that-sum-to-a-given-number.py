class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # for i in range(num//2):
        #     if i + i+1 + i+2 == num:
        #         return [i, i+1, i+2]
        # return []

        x = (num-3) / 3
        return [int(x), int(x+1), int(x+2)] if floor(x) == ceil(x) else []