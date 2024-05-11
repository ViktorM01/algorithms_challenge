#include <vector>

class Solution {
public:
    std::vector<int> buildArray(std::vector<int>& nums) {
        std::vector<int> rev_lst;

        for (int n : nums) {
            rev_lst.push_back(nums[n]);
        }

        return rev_lst;
    }
};
