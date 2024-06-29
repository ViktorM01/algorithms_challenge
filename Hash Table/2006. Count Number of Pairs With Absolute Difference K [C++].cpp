class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        int cnt = 0;
        unordered_map<int, int> freq;

        for (int n : nums) {
            if (freq.find(n + k) != freq.end()) {
                cnt += freq[n + k];
            }
            if (freq.find(n - k) != freq.end()) {
                cnt += freq[n - k];
            }
            freq[n]++;
        }
        return cnt;
    }
};
