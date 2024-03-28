class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        sum_shift = sum(shifts)
        output = ""
        i = 0
        
        while i < len(shifts):
            output += alphabet[(ord(s[i]) - ord('a') + sum_shift) % 26]
            sum_shift -= shifts[i]
            i += 1
            
        return output
            
        