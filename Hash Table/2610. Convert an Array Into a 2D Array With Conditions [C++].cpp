#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<std::vector<int>> findMatrix(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        std::vector<std::vector<int>> ans;

        for (int num : nums) {
            if (freq[num] >= ans.size()) {
                ans.push_back({});
            }
            ans[freq[num]].push_back(num);
            freq[num]++;
        }

        return ans;
    }
};
