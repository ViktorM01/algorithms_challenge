class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            s[i] = s[i].lower()
        return ''.join(s)
