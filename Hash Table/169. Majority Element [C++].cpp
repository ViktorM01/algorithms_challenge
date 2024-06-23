#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> count_map;
        for (int num : nums) {
            count_map[num]++;
        }
        int majority_element = nums[0];
        int max_count = 0;
        for (const auto& pair : count_map) {
            if (pair.second > max_count) {
                max_count = pair.second;
                majority_element = pair.first;
            }
        }
        return majority_element;
    }
};
