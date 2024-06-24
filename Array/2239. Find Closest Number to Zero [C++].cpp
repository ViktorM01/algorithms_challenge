#include <vector>
#include <cmath>
#include <algorithm>

class Solution {
public:
    int findClosestNumber(std::vector<int>& nums) {
        int closest = INT_MAX;
        
        for (int num : nums) {
            if (std::abs(num) < std::abs(closest) || 
                (std::abs(num) == std::abs(closest) && num > closest)) {
                closest = num;
            }
        }
        
        return closest;
    }
};
