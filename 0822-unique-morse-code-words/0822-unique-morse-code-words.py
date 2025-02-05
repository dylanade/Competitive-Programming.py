class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        answer = set()
        for word in words:
            morse_word = ""
            for char in word:
                morse_word += morse[ord(char.lower()) - 97]

            answer.add(morse_word)

        return len(answer)
