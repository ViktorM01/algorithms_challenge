class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
            if dic[i] == 2:
                return i
        return ''
