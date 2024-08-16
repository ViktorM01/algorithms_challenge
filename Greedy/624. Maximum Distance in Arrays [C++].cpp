class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int min_ = arrays[0][0];
        int max_ = arrays[0].back();
        int max_dist = 0;

        for (int i = 1; i < arrays.size(); ++i) {
            max_dist = max(max_dist, abs(arrays[i].back() - min_));
            max_dist = max(max_dist, abs(max_ - arrays[i][0]));

            min_ = min(min_, arrays[i][0]);
            max_ = max(max_, arrays[i].back());
        }

        return max_dist;
    }
};
