class Solution {
public:
    int removePalindromeSub(string s) {
        string reversed_s = s;
        reverse(reversed_s.begin(), reversed_s.end());
        if (s == reversed_s) {
            return 1;
        } else {
            return 2;
        }
    }
};
