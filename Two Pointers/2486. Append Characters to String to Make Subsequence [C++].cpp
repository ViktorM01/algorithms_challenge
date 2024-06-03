class Solution {
public:
    int appendCharacters(string s, string t) {
        int s_idx = 0, t_idx = 0;
        int s_l = s.length(), t_l = t.length();

        while (s_idx < s_l && t_idx < t_l) {
            if (s[s_idx] == t[t_idx]) {
                t_idx++;
            }
            s_idx++;
        }

        return t_l - t_idx;
    }
};
