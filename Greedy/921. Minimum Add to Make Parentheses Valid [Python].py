class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l_p, c_p = 0, 0
        for i in s:
            if i == '(':
                l_p += 1
            elif i == ')' and l_p > 0:
                l_p -= 1
            else:
                c_p += 1

        return l_p + c_p
