class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        unfairness = float("inf") # minimum unfairness
        distribution = [0] * k # distribution between k children

        def backtrack(i): # init to start from first child
            nonlocal unfairness
            max_cookies = max(distribution)

            # base cases
            if i == len(cookies):
                unfairness = min(unfairness, max_cookies)
                return
            
            if unfairness <= max_cookies:
                return

            # decisions
            for j in range(k):
                distribution[j] += cookies[i] # distribute it to the first child
                backtrack(i + 1) # distribute it to the next child
                distribution[j] -= cookies[i] # removing cookie from first child

        backtrack(0)
        return unfairness