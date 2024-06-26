class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_table = {key: s.count(key) for key in set(s)}
        l = list(hash_table.values())
        return [l[0]]*len(l) == l
