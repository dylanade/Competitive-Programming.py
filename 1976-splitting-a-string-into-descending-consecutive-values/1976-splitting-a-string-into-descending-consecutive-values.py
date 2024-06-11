class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(i, prev):
            if i == n:
                return True
            
            for j in range(i, n):
                val = int(s[i:j+1])
                if val + 1 == prev and dfs(j+1, val):
                    return True
            return False

        for i in range(n - 1):
            val = int(s[:i+1])
            if dfs(i+1, val): return True

        return False

                

        
        