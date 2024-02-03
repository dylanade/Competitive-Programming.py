import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############

#taking integer input
def inp():
    return(int(input()))
    
#taking list input
def inlt():
    return(list(map(int,input().split())))
    
#taking string input but returns a char list
def insr():
    s = input()
    return(list(s[:len(s) - 1]))

#for taking space separated integers
def invr():
    return(map(int,input().split()))
    
def solution():
    n = inp()
    count = 0
    for i in range(n):
        problem = list(map(int,input().split()))
        know = sum(problem)
        if (know > 1):
            count+=1
        
    return count

print(solution())
        
