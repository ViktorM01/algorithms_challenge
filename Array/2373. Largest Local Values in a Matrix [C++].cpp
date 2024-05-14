#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        for (int i = 1; i < n - 1; ++i) {
            for (int j = 1; j < n - 1; ++j) {
                int t = 0;
                for (int k = i - 1; k <= i + 1; ++k) {
                    for (int l = j - 1; l <= j + 1; ++l) {
                        t = max(t, grid[k][l]);
                    }
                }
                grid[i - 1][j - 1] = t;
            }
        }
        n = grid.size();
        grid.resize(n - 2);
        for (auto& row : grid) {
            row.resize(n - 2);
        }
        return grid;
    }
};
