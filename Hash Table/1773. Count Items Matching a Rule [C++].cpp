#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    int countMatches(std::vector<std::vector<std::string>>& items, std::string ruleKey, std::string ruleValue) {
        int cnt = 0;
        std::unordered_map<std::string, int> d = {{"type", 0}, {"color", 1}, {"name", 2}};
        
        for (const auto& item : items) {
            if (item[d[ruleKey]] == ruleValue) {
                cnt++;
            }
        }
        
        return cnt;
    }
};
