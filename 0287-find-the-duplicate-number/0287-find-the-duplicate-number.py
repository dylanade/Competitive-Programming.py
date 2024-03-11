sys.stdout = open('user.out', 'w')
for nums in map(loads, stdin):
    print(Counter(nums).most_common(1)[0][0])
        
        