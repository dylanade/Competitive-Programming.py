#User function Template for python3

def isSubset( a1, a2, n, m):
    b1 = list(a1)
    b2 = list(a2)
    
    for i in range(len(b2)):
        if (b2[i] not in b1):
            return 'No'
        if (b2[i] in b1):
            b1.remove(b2[i])
            
    return 'Yes'
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
