class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {var: s.count(var) for var in set(s)}
        s2 = {var: t.count(var) for var in set(t)}
        return s1 == s2
