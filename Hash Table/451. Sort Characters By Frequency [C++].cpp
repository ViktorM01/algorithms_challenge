class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> dct;
        for (char c : s) {
            dct[c]++;
        }
        vector<pair<char, int>> pars;
        for (auto& it : dct) {
            pars.push_back(it);
        }
        sort(pars.begin(), pars.end(), [](pair<char, int>& a, pair<char, int>& b) {
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        });
        string ans = "";
        for (auto& p : pars) {
            ans += string(p.second, p.first);
        }
        return ans;
    }
};
