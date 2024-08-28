class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        answer = []
        dictionary.sort()
        sentence = sentence.split()

        for word in sentence:
            flag = 0
            for x in dictionary:
                if word.startswith(x):
                    answer.append(x)
                    flag = 1
                    break

            if flag == 0: 
                answer.append(word)

        return " ".join(answer)