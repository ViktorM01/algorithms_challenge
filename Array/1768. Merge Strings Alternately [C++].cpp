#include <iostream>
#include <string>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        std::string ans = "";
        int maxLength = std::max(word1.size(), word2.size());
        for (int i = 0; i < maxLength; ++i) {
            if (i < word1.size()) {
                ans += word1[i];
            }
            if (i < word2.size()) {
                ans += word2[i];
            }
        }
        return ans;
    }
};
