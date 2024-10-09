class Solution {
public:
    int minAddToMakeValid(std::string s) {
        int l_p = 0, c_p = 0;

        for (char i : s) {
            if (i == '(') {
                l_p++;
            } else if (i == ')' && l_p > 0) {
                l_p--;
            } else {
                c_p++;
            }
        }
        return l_p + c_p;
    }
};
