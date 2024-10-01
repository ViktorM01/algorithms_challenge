#include <vector>
#include <unordered_map>

class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        std::unordered_map<int, int> dct_;
        for (int num : nums) {
            dct_[num]++;
        }
        for (const auto& entry : dct_) {
            if (entry.second > 2) {
                return false;
            }
        }
        return true;
    }
};
