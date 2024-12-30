class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int prefix_dp = values[0], n = values.size(), max_ans = 0;
        for (int i = 1; i < n; i++) {
            max_ans = max(max_ans, values[i] - i + prefix_dp);
            prefix_dp = max(prefix_dp, values[i] + i);
        }
        return max_ans;
    }
};
