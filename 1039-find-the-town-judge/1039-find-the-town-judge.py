class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge has n-1 incoming and 0 outgoing
        check_1 = defaultdict(int) # incoming
        check_2 = defaultdict(int) # outgoing

        for a, b in trust:
            check_1[b] += 1
            check_2[a] += 1
            
        for i in range(1, n+1):
            if check_1[i] == n-1 and check_2[i] == 0:
                return i
        
        return -1