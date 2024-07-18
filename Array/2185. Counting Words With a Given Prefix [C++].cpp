class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int n = pref.size();
        int cnt = 0;

        for (const std::string& word : words) {
            if (word.substr(0, n) == pref) {
                cnt++;
            }
        }
        return cnt;
    }
};
