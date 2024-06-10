#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    std::vector<int> distinctDifferenceArray(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> prefixUnique(n, 0);
        std::vector<int> suffixUnique(n, 0);
        std::unordered_set<int> seen;

        for (int i = 0; i < n; ++i) {
            seen.insert(nums[i]);
            prefixUnique[i] = seen.size();
        }

        seen.clear();

        for (int i = n - 1; i >= 0; --i) {
            seen.insert(nums[i]);
            suffixUnique[i] = seen.size();
        }

        std::vector<int> result(n);
        for (int i = 0; i < n; ++i) {
            int suffixCount = (i + 1 < n) ? suffixUnique[i + 1] : 0;
            result[i] = prefixUnique[i] - suffixCount;
        }

        return result;
    }
};
