class Solution:
    def shortestCompletingWord(self, licenseChars: str, words: List[str]) -> str:
        licenseChars = [char.lower() for char in licenseChars if char.isalpha()]
        countChar = collections.Counter(licenseChars)
        answer = []

        for word in words:
            skip = False
            
            for char in countChar:
                if word.count(char) < countChar[char]:
                    skip = True
                    break

            if not skip:
                answer.append(word)
        
        answer.sort(key=len)
        return answer[0]