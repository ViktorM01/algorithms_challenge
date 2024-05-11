#include <vector>

class Solution {
public:
    int numIdenticalPairs(std::vector<int>& nums) {
        int sum_val = 0;
        for (size_t i = 0; i < nums.size(); ++i) {
            for (size_t j = i + 1; j < nums.size(); ++j) {
                if (nums[i] == nums[j]) {
                    sum_val++;
                }
            }
        }
        return sum_val;
    }
};
