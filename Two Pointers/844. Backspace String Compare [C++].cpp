class Solution {
public:
    bool backspaceCompare(string s, string t) {
        vector<char> s_vec, t_vec;
        for (char c : s) {
            if (c == '#') {
                if (!s_vec.empty()) {
                    s_vec.pop_back();
                }
            } else {
                s_vec.push_back(c);
            }
        }

        for (char c : t) {
            if (c == '#') {
                if (!t_vec.empty()) {
                    t_vec.pop_back();
                }
            } else {
                t_vec.push_back(c);
            }
        }

        return s_vec == t_vec;
    }
};
