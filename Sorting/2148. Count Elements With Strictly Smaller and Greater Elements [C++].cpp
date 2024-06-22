#include <vector>
#include <algorithm>

class Solution {
public:
    int countElements(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int max_ab = *std::max_element(nums.begin(), nums.end());
        int min_ab = *std::min_element(nums.begin(), nums.end());
        
        int max_count = std::count(nums.begin(), nums.end(), max_ab);
        int min_count = std::count(nums.begin(), nums.end(), min_ab);
        
        return std::max(0, static_cast<int>(nums.size()) - max_count - min_count);
    }
};
