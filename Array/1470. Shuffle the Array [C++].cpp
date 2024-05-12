#include <vector>

class Solution {
public:
    std::vector<int> shuffle(std::vector<int>& nums, int n) {
        int i = 0, j = n;
        std::vector<int> ans;

        while (i <= n - 1) {
            ans.push_back(nums[i]);
            ans.push_back(nums[j]);
            i++;
            j++;
        }

        return ans;
    }
};
