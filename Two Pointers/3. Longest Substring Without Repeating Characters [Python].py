class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len = 0, 0
        unique = {}

        for r in range(len(s)):
            if s[r] in unique and unique[s[r]] >= l:
                l = unique[s[r]] + 1
            unique[s[r]] = r
            max_len = max(max_len, r - l + 1)

        return max_len
