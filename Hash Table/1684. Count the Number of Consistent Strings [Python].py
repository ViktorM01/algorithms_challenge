class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = set(allowed)
        s = 0
        for i in words:
            if set(i).issubset(al):
                s += 1
        return s
