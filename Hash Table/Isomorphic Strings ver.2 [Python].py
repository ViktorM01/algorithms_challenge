class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dict1, dict2 = dict(), dict()

        for i in range(len(s)):
            if s[i] not in dict1 and t[i] not in dict2:
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
            elif s[i] in dict1 and dict1[s[i]] != t[i]:
                return False
            elif t[i] in dict2 and dict2[t[i]] != s[i]:
                return False

        return True
