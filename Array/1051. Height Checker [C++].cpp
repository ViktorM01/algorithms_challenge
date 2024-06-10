#include <vector>
#include <algorithm>

class Solution {
public:
    int heightChecker(std::vector<int>& heights) {
        std::vector<int> lst_sort = heights;
        std::sort(lst_sort.begin(), lst_sort.end());
        int cnt = 0;
        for (size_t i = 0; i < heights.size(); ++i) {
            if (heights[i] != lst_sort[i]) {
                ++cnt;
            }
        }
        return cnt;
    }
};
