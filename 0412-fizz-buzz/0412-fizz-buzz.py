class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [i+1 for i in range(n)]
        for i in ans:
            if i%15 == 0:
                ans[i-1] = "FizzBuzz"
            elif i%3 == 0:
                ans[i-1] = "Fizz"
            elif i%5 == 0:
                ans[i-1] = "Buzz"
            else:
                ans[i-1] = str(i)
        return ans
        