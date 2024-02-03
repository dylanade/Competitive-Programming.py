class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        tail = []
        merged = []
        word1Chars = list(word1)
        word2Chars = list(word2)
        
        #get the length of each words
        len_1 = len(word1Chars)
        len_2 = len(word2Chars)
        
        #merge the list
        minLen = min(len_1, len_2)
        for i in range(minLen*2):
            if (i % 2 == 0):
                merged.append(word1Chars[i/2])
            else:
                merged.append(word2Chars[(i-1)/2])
                
        #get the tail of the list
        if (len_1 > len_2):
            tail = word1Chars[len_2:]
        else:
            tail = word2Chars[len_1:]
            
        #combine the tail and the merged list
        merged = merged + tail

        return "".join(merged)


