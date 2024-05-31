#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> flipAndInvertImage(std::vector<std::vector<int>>& image) {
        std::vector<std::vector<int>> result;
        for (auto& row : image) {
            std::reverse(row.begin(), row.end());
            for (auto& element : row) {
                element = element == 1 ? 0 : 1;
            }
            result.push_back(row);
        }
        return result;
    }
};
