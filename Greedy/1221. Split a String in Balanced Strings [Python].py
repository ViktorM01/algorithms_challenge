class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dct_ = {"L": 0, "R": 0}
        k = 0
        for i in s:
            dct_[i] += 1
            if dct_['L'] == dct_['R']:
                k += 1
        return k
