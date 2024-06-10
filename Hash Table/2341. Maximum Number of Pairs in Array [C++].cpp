#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> numberOfPairs(std::vector<int>& nums) {
        std::unordered_map<int, int> countMap;
        for (int num : nums) {
            countMap[num]++;
        }

        int pairs = 0;
        int leftovers = 0;
        for (auto& entry : countMap) {
            pairs += entry.second / 2;
            leftovers += entry.second % 2;
        }

        return {pairs, leftovers};
    }
};
