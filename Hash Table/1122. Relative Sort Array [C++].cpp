#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> relativeSortArray(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::unordered_map<int, int> countMap;
        std::vector<int> result;

        for (int num : arr1) {
            countMap[num]++;
        }

        for (int num : arr2) {
            result.insert(result.end(), countMap[num], num);
            countMap.erase(num);
        }

        std::vector<int> remaining;
        for (const auto& entry : countMap) {
            remaining.insert(remaining.end(), entry.second, entry.first);
        }
        std::sort(remaining.begin(), remaining.end());
        result.insert(result.end(), remaining.begin(), remaining.end());

        return result;
    }
};
