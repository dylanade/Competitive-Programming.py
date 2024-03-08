class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        indices = [i for i in range(n)]
        
        def find(x):
            if x != indices[x]:
                indices[x] = find(indices[x])
            return indices[x]
        
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                indices[rx] = ry
                
        for i,j in pairs:
            union(i,j)
        
        group = collections.defaultdict(list)
        for i in range(n):
            group[find(i)] += s[i],
        
        for j in group.values():
            j.sort()
            
        count = collections.Counter()
        ans = ["" for _ in range(n)]
        for i in range(n):
            ans[i] = group[find(i)][count[find(i)]]
            count[find(i)] += 1
            
        return "".join(ans)
            