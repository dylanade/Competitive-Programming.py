class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        print("decimal = binary")
        for i in range(n + 1):
            print(f"{i} = {bin(i)[2:]}")
            ans.append(bin(i).count('1'))
        return ans
