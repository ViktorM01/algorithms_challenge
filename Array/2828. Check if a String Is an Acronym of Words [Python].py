class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        l = ''
        for i in words:
            l += i[0]
        return True if l == s else False
