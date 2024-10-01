#include <vector>

class Solution {
public:
    vector<int> findPeaks(vector<int>& mountain) {
        std::vector<int> peaks;
        for (int i = 1; i < mountain.size() - 1; ++i) {
            if (mountain[i - 1] < mountain[i] && mountain[i + 1] < mountain[i]) {
                peaks.push_back(i);
            }
        }
        return peaks;
    }
};
