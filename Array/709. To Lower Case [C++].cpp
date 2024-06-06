#include <iostream>
#include <string>
#include <cctype> // for std::tolower

class Solution {
public:
    std::string toLowerCase(const std::string &s) {
        std::string result = s;
        for (size_t i = 0; i < result.size(); ++i) {
            result[i] = std::tolower(result[i]);
        }
        return result;
    }
};
