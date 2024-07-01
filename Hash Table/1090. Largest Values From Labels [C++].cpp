class Solution {
public:
    int largestValsFromLabels(vector<int>& values, vector<int>& labels, int numWanted, int useLimit) {
        unordered_map<int, int> use_lim;
        int val = 0;
        vector<pair<int, int>> zp;
        for (int i = 0; i < values.size(); i++) {
            zp.push_back({values[i], labels[i]});
        }
        sort(zp.begin(), zp.end(), [](pair<int, int>& a, pair<int, int>& b) {
            return a.first > b.first;
        });
        for (auto i : zp) {
            if (numWanted == 0) {
                return val;
            }
            if (use_lim.find(i.second) == use_lim.end() || use_lim[i.second] < useLimit) {
                val += i.first;
                numWanted--;
                if (use_lim.find(i.second) == use_lim.end()) {
                    use_lim[i.second] = 1;
                } else {
                    use_lim[i.second]++;
                }
            }
        }
        return val;
    }
};
