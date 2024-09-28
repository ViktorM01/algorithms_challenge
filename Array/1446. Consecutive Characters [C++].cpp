class Solution {
public:
    int maxPower(string s) {
        int cnt = 1, max_cnt = 1;
        for (int i = 1; i < s.length(); ++i) {
            if (s[i-1] == s[i]) {
                cnt++;
                max_cnt = max(cnt, max_cnt);
            } else {
                cnt = 1;
            }
        }
        return max_cnt;
    }
};
