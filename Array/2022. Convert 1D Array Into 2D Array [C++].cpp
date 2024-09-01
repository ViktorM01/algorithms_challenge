class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int len = original.size();
        if (m * n != len) {
            return {};
        }

        vector<vector<int>> result;
        for (int i = 0; i < m; ++i) {
            vector<int> row(original.begin() + i * n, original.begin() + (i + 1) * n);
            result.push_back(row);
        }
        return result;
    }
};
