class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for w in strs:
            cnt = [0] * 26

            for s in w:
                cnt[ord(s) - ord('a')] += 1
        
            group[tuple(cnt)].append(w)

        return group.values()
