#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>

class Solution {
public:
    int minNumber(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> set2(nums2.begin(), nums2.end());
        
        int min1 = INT_MAX;
        int min2 = INT_MAX;
        int minIntersection = INT_MAX;
        bool foundIntersection = false;
        
        for (int num : nums1) {
            if (set2.count(num)) {
                foundIntersection = true;
                minIntersection = std::min(minIntersection, num);
            }
            min1 = std::min(min1, num);
        }
        
        for (int num : nums2) {
            min2 = std::min(min2, num);
        }
        
        if (foundIntersection) {
            return minIntersection;
        }

        if (min1 < min2) {
            return std::stoi(std::to_string(min1) + std::to_string(min2));
        } else {
            return std::stoi(std::to_string(min2) + std::to_string(min1));
        }
    }
};
