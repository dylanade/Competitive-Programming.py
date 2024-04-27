class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
            
        add_one = False
        tot_len = 0
        for letter in count.keys():
            if count[letter]%2 == 1:
                add_one = True
                tot_len += count[letter] - 1
            else:
                tot_len += count[letter]
        
        if add_one:
            tot_len += 1
            
        return tot_len
                
                
        