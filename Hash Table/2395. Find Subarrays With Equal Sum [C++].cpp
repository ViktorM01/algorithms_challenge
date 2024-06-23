#include <vector>
#include <unordered_set>

class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int end = 0; end < nums.size() - 1; ++end) {
            int sum = nums[end] + nums[end + 1];
            if (seen.find(sum) != seen.end()) {
                return true;
            }
            seen.insert(sum);
        }
        return false;
    }
};
