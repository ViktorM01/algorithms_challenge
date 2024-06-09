#include <vector>
#include <unordered_map>

class Solution {
public:
    int subarraysDivByK(std::vector<int>& nums, int k) {
        int cnt = 0;
        std::unordered_map<int, int> pref_map;
        pref_map[0] = 1;
        int pref_sum = 0;

        for (int n : nums) {
            pref_sum += n;
            int mod = (pref_sum % k + k) % k; 
            if (pref_map.find(mod) != pref_map.end()) {
                cnt += pref_map[mod];
            }
            ++pref_map[mod];
        }
        return cnt;
    }
};
