class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        lst = [idx for idx in range(len(s1)) if s1[idx] != s2[idx]]

        return len(lst) == 2 and s1[lst[0]] == s2[lst[1]] and s1[lst[1]] == s2[lst[0]]
