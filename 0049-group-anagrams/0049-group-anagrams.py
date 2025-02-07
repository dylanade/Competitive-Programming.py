class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        print(group)

        for word in strs:
            group[tuple(sorted(word))].append(word)

        return list(group.values())