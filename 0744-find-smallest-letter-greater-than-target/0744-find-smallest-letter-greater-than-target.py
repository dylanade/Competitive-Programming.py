class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter != target and letter > target:
                return letter
        return letters[0]
        