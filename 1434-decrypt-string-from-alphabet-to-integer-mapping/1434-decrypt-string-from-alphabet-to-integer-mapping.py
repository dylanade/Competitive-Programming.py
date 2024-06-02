class Solution:
    def freqAlphabets(self, s: str) -> str:
        letter_map = collections.defaultdict(str)

        for i in range(97, 123):
            letter_map[i%96] = chr(i)
        
        answer = []
        for i, digit in enumerate(s):
            if digit == "#":
                answer.pop()
                answer.pop()
                answer.append(letter_map[int(s[i-2] + s[i-1])])
            else:
                answer.append(letter_map[int(digit)])
        
        return "".join(answer)


            

