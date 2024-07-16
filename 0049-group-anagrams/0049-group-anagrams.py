class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list) # charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a - z
            for c in s:
                count[ord(c) - ord("a")] += 1 
            answer[tuple(count)].append(s)

        return answer.values()

