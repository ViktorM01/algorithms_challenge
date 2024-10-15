class Solution {
public:
    long long minimumSteps(string s) {
        int black = 0;
        long long ans = 0;
        for (char el : s) {
            if (el == '0') {
                ans += black;
            } else {
                black++;
            }
        }
        return ans;
    }
};
