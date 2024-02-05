if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for i in range(N):
        data = list(input().split())
        
        if (data[0] == "insert"):
            arr.insert(int(data[1]), int(data[2]))
    
        elif (data[0] == "print"):
            print(arr)
            
        elif (data[0] == "remove"):
            arr.remove(int(data[1]))
            
        elif (data[0] == "append"):
            arr.append(int(data[1]))
            
        elif (data[0] == "sort"):
            arr.sort()
            
        elif (data[0] == "pop"):
            arr.pop()
        
        elif (data[0] == "reverse"):
            arr.reverse()
    
#LINK: https://www.hackerrank.com/challenges/python-lists/submissions/code/368347213
