class Solution:
    def makeFancyString(self, s: str) -> str:
        flst = []
        count = 0
        for i in range(len(s)):
            if s[i-1] == s[i]:
                count += 1
            else:
                count = 1
            if count < 3:
                flst.append(s[i])
        return "".join(flst)
