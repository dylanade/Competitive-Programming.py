# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phoneBook = {}

for i in range(n):
    data = input().split()
    phoneBook[data[0]] = data[1]
        
while True:
    try:
        name = input()
        if (name in phoneBook):
            print(f'{name}={phoneBook.get(name)}')
        else:
            print('Not found')
    except EOFError:
        break
