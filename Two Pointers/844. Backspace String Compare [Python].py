class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_lst, t_lst = [], []

        for i in range(len(s)):
            if s[i] == '#':
                if len(s_lst) > 0:
                    s_lst.pop()
            else:
                s_lst.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if len(t_lst) > 0:
                    t_lst.pop()
            else:
                t_lst.append(t[i])

        return t_lst == s_lst
