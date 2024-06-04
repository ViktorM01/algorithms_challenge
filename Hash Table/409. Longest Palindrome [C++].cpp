#include <unordered_set>
#include <string>

class Solution {
public:
    int longestPalindrome(std::string s) {
        std::unordered_set<char> set_s;
        int le = 0;

        for (char ch : s) {
            if (set_s.find(ch) != set_s.end()) {
                set_s.erase(ch);
                le += 2;
            } else {
                set_s.insert(ch);
            }
        }

        if (!set_s.empty()) {
            le += 1;
        }

        return le;
    }
};
