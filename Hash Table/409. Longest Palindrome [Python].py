class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_s = set()
        le = 0

        for ch in s:
            if ch in set_s:
                set_s.remove(ch)
                le += 2
            else:
                set_s.add(ch)

        if set_s:
            le += 1

        return le
