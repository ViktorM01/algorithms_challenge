#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    std::string kthDistinct(std::vector<std::string>& arr, int k) {
        std::unordered_map<std::string, int> frequency;
        for (const auto& str : arr) {
            frequency[str]++;
        }

        std::vector<std::string> distinct;
        for (const auto& str : arr) {
            if (frequency[str] == 1) {
                distinct.push_back(str);
            }
        }

        return k > distinct.size() ? "" : distinct[k - 1];
    }
};
