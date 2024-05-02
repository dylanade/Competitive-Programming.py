class Solution:
    def Pow(self, x: float, n: int) -> float:
        MOD = 10**9+7
        if n == 0: 
            return 1
        if n<0:
            return self.Pow(1/x,-n)
        if not n%2:
            return self.Pow((x*x)%MOD, n//2)
        else:
            return x*self.Pow((x*x)%MOD, (n-1)//2)
        
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        count_even = self.Pow(5, (n//2 + n%2)) % MOD
        count_odd = self.Pow(4, (n//2)) % MOD
        return (count_even * count_odd) % MOD
        