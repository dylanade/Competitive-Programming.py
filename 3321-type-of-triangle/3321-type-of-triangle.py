class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        if (a + b) > c and (a + c) > b and (b + c) > a:
            if a != b and a != c and c != b:
                return "scalene"
            elif a == b and a == c and c == b:
                return "equilateral"
            else:
                return "isosceles"
        else:
            return "none"

        