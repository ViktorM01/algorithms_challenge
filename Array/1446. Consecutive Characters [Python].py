class Solution:
    def maxPower(self, s: str) -> int:
        cnt, max_cnt = 1, 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        return max_cnt
