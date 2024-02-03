class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        value = 0
        
        #getting the ASCII value using ord() for each character in the list s
        for char in s:
            value ^= ord(char)
        
        #using bitwise XOR function to get odd character
        for char in t:
            value ^= ord(char)
            
        #convert value into char
        return chr(value)
        