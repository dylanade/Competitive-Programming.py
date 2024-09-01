class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0

        def getMask(word: str) -> int:
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - ord('a')
            return mask

        masks = [getMask(word) for word in words]

        for i in range(len(words)):
            for j in range(i):
                if not (masks[i] & masks[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

# For each pair of words, the bitwise AND of their bit masks is computed using the '&' operator. If the result of the bitwise AND is 0, then the two words do not share any common letters, and their product is compared to the current maximum product stored in the ans variable. If the product is greater than the current maximum, it is stored in the ans variable.