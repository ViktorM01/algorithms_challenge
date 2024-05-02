#include <vector>
#include <algorithm>
#include <limits>

class Solution {
public:
    int findMaxK(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int l = 0;
        int r = nums.size() - 1;
        int max_k = std::numeric_limits<int>::min();
        
        while (l < r) {
            if (nums[l] + nums[r] == 0) {
                max_k = std::max(max_k, nums[r]);
                l++;
                r--;
            }
            if (nums[l] + nums[r] < 0) {
                l++;
            } else {
                r--;
            }
        }
        return max_k != std::numeric_limits<int>::min() ? max_k : -1;
    }
};
