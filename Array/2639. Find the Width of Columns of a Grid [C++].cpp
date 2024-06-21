#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    std::vector<int> findColumnWidth(std::vector<std::vector<int>>& grid) {
        int n = grid[0].size();
        std::vector<int> lst(n, 0);

        for (const auto& row : grid) {
            for (int j = 0; j < n; ++j) {
                int width = std::to_string(row[j]).length();
                if (width > lst[j]) {
                    lst[j] = width;
                }
            }
        }

        return lst;
    }
};
