class Solution:
    def predict(self, nums, start, end, turn):
            if start == end:
                return turn*nums[start]
            p1 = turn * nums[start] + self.predict(nums, start+1, end, -turn)
            p2 = turn * nums[end] + self.predict(nums, start, end-1, -turn)
            return turn*max(turn*p1, turn*p2)

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.predict(nums,0,len(nums)-1,1) >= 0

