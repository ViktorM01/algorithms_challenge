#include <vector>
#include <algorithm>

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> count(n, 0);
        for (int num : nums) {
            count[num - 1]++;
        }

        int duplicated = -1, missing = -1;
        for (int i = 0; i < n; ++i) {
            if (count[i] == 2) {
                duplicated = i + 1;
            } else if (count[i] == 0) {
                missing = i + 1;
            }
        }
        return {duplicated, missing};
    }
};
