#include <vector>
#include <string>

class Solution {
public:
    std::string restoreString(std::string s, std::vector<int>& indices) {
        std::string result(s.size(), ' ');
        for (int i = 0; i < indices.size(); ++i) {
            result[indices[i]] = s[i];
        }     
        return result;
    }
};
