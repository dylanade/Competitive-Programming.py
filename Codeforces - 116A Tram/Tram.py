cases = int(input())
capacity = 0
min_capacity = 0

for i in range(cases):
    a, b = list(map(int, input().split()))
    
    capacity -= a
    capacity += b
    
    if capacity > min_capacity:
        min_capacity = capacity
    
print(min_capacity)

#LINK: https://codeforces.com/contest/116/submission/245640588
