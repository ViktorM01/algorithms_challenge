class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_idx, t_idx = 0, 0
        s_l, t_l = len(s), len(t)

        while s_idx < s_l and t_idx < t_l:
            if s[s_idx] == t[t_idx]:
                t_idx += 1
            s_idx += 1

        return t_l - t_idx
