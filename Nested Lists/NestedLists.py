if __name__ == '__main__':
    
    dictionary = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dictionary[name] = score
        
    scores = sorted(dictionary.values())
    lowest = scores[0]
    sec_lowest = scores[1]
    
    index = 0
    while (sec_lowest == lowest):
        sec_lowest = scores[index]
        index += 1
    
    answer = []
    for key in dictionary:
        if (dictionary.get(key) == sec_lowest):
            answer.append(key)
            
    for student in sorted(answer):
        print(student)

#LINK: https://www.hackerrank.com/challenges/nested-list/submissions/code/368345901
