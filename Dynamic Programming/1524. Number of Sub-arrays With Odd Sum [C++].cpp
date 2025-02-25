class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        long long cnt = 0, prefSum = 0, mod = 1000000007;
        for (int num : arr) {
            prefSum += num;
            if (prefSum % 2 != 0) {
                cnt++;
            }
        }
        cnt = (cnt * (arr.size() - cnt) + cnt) % mod;
        return static_cast<int>(cnt);
    }
};
