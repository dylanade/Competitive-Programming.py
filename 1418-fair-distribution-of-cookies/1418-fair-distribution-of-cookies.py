class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        unfairness = float("inf") # minimum unfairness
        distribution = [0] * k # distribution between k children

        def backtrack(i): # init to start 
            nonlocal unfairness

            # base cases
            if i == len(cookies):
                unfairness = min(unfairness, max(distribution))
                return
            
            if unfairness <= max(distribution):
                return

            # decisions
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)
        return unfairness


