#include <vector>
#include <algorithm>

class Solution {
public:
    int minIncrementForUnique(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        for (size_t i = 0; i < nums.size() - 1; ++i) {
            if (nums[i + 1] <= nums[i]) {
                ans += nums[i] - nums[i + 1] + 1;
                nums[i + 1] += nums[i] - nums[i + 1] + 1;
            }
        }
        return ans;
    }
};
