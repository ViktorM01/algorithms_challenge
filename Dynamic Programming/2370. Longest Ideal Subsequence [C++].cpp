class Solution {
public:
    int longestIdealString(string s, int k) {
        int dp[27] = {0};
        int n = s.length();
        int max_val = -__INT_MAX__;

        for (int i = 0; i < n; i++) {
            char sub_s = s[i];
            int ind = sub_s - 'a';
            int m_v = -__INT_MAX__;

            int l = max((ind - k), 0);
            int r = min((ind + k), 26);

            for (int j = l; j <= r; j++) {
                m_v = max(m_v, dp[j]);
            }

            dp[ind] = m_v + 1;
            max_val = max(max_val, dp[ind]);
        }

        return max_val;
    }
};
