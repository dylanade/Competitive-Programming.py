class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #declaring a dictionary variable to store {char: occurence}
        dictionary = {}
        
        #populating dictionary
        for char in s:
            dictionary[char] = dictionary.get(char, 0) + 1
        
        #searching through dictionary to get first unique char
        for i in range(len(s)):
            if (dictionary.get(s[i]) == 1):
                return i
        
        #if can't find unique char return -1
        return -1