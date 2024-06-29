class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = sum(ord(i) for i in s)
        sum_t = sum(ord(j) for j in t)
        return chr(sum_t - sum_s)
