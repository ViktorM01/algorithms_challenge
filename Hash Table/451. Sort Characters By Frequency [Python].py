class Solution:
    def frequencySort(self, s: str) -> str:
        dct_ = {key: s.count(key) for key in set(s)}
        pars = sorted(dct_.items(), key=lambda x: (-x[1], x[0]))
        ans = ''
        for i in pars:
            ans += i[0] * i[1]
        return ans
