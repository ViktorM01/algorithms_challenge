class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        c = [0] * 1024
        res, pref_xor = 0, 0
        c[pref_xor] = 1

        for s in word:
            s_indx = ord(s) - ord('a')
            pref_xor ^= 1 << s_indx
            res += c[pref_xor]
            for i in range(10):
                res += c[pref_xor ^ (1 << i)]
            c[pref_xor] += 1

        return res
