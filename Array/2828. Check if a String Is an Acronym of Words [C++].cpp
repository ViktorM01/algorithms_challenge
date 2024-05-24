#include <vector>
#include <string>

class Solution {
public:
    bool isAcronym(std::vector<std::string>& words, std::string s) {
        std::string l = "";
        for (const auto& word : words) {
            l += word[0];
        }
        return l == s;
    }
};
