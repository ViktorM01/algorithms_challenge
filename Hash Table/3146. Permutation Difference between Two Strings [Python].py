class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        dic1, dic2 = dict(), dict()
        dic1 = {val: i for i, val in enumerate(s)}
        dic2 = {val: i for i, val in enumerate(t)}

        # k = {key: abs(dic1.get(key, 0) - dic2.get(key, 0)) for key in set(dic1) | set(dic2)}
        # return k

        sum_f = 0
        for ch in s:
            diff = abs(dic1[ch]-dic2[ch])
            sum_f += diff

        return sum_f
