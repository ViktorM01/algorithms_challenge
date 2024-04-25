class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 27
        n = len(s)
        
        for i in range(n):
            sub_s = s[i]
            ind = ord(sub_s) - ord('a')

            m_v = float('-inf')

            l = max((ind-k), 0)
            r = min((ind+k), 26)

            for j in range(l, r+1):
                m_v = max(m_v, dp[j])

            dp[ind] = m_v + 1

        return max(dp)
