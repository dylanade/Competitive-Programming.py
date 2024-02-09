n, k = list(map(int,input().split()))
answer = n
            
for i in range(k):
    digit = answer % 10
    if (digit > 0):
        answer-=1
    else:
        answer/=10
                
print(str(int(answer)))

#LINK: https://codeforces.com/contest/977/submission/245639698
