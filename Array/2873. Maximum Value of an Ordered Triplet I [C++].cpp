class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long ans = 0, max_dif = 0, max_val = 0;

        for (int k : nums) {
            long long k_ll = static_cast<long long>(k);
            ans = max(ans, k_ll * max_dif);
            max_dif = max(max_dif, max_val - k_ll);
            max_val = max(max_val, k_ll);
        }
        return ans;
    }
};
