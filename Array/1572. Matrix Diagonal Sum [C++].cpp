#include <vector>

class Solution {
public:
    int diagonalSum(std::vector<std::vector<int>>& mat) {
        int n = mat.size();
        int f = 0;
        
        for (int i = 0; i < n; ++i) {
            f += mat[i][i] + mat[i][n - 1 - i];
        }
        
        if (n % 2 == 1) {
            f -= mat[n / 2][n / 2];
        }
        
        return f;
    }
};
