class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = 0
        i = 0  # Start index of the current substring
        while i < len(word):
            # Check if the current substring starts with 'a' and ensure we haven't reached the end
            if word[i] == 'a':
                unique_vowels = 1  # 'a' found, so we have one unique vowel
                j = i + 1  # Next character to check
                
                # Loop to find the length of the beautiful substring
                while j < len(word) and word[j] >= word[j - 1]:
                    # Increment unique vowels if we find a new vowel in order
                    if word[j] > word[j - 1]:
                        unique_vowels += 1
                    j += 1
                
                # Update result if all five vowels are found in order
                if unique_vowels == 5:
                    ans = max(ans, j - i)
                i = j  # Move to the end of the current beautiful substring
            else:
                i += 1  # Not starting with 'a', skip to the next character
        
        return ans
                
                
                
        
        