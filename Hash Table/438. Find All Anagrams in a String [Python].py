class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lst = []
        freq_s = [0] * 26
        freq_p = [0] * 26

        if len(s) < len(p):
            return lst

        for i in range(len(p)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_p[ord(p[i]) - ord('a')] += 1

        start, end = 0, len(p)

        if freq_s == freq_p:
            lst.append(start)

        while end < len(s):
            freq_s[ord(s[start]) - ord('a')] -= 1
            freq_s[ord(s[end]) - ord('a')] += 1

            if freq_s == freq_p:
                lst.append(start + 1)

            start += 1
            end += 1

        return lst
