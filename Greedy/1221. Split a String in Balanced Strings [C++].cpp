class Solution {
public:
    int balancedStringSplit(const std::string& s) {
        int countL = 0, countR = 0, k = 0;
        for (char c : s) {
            if (c == 'L') {
                countL++;
            } else if (c == 'R') {
                countR++;
            }
            if (countL == countR) {
                k++;
            }
        }
        return k;
    }
};
